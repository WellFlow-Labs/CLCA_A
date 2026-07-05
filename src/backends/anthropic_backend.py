from __future__ import annotations

import os
import time
import logging
from typing import Optional

from .base import LLMBackend, LLMResponse

try:
    from anthropic import Anthropic
except ImportError as e:
    raise ImportError(
        "The anthropic python package is required. Install with: pip install anthropic"
    ) from e


logger = logging.getLogger(__name__)


class AnthropicBackend(LLMBackend):
    """
    Anthropic backend with:
      - optional long-context mode (1M tokens)
      - adaptive rate limiting
      - unified LLMBackend interface

    Long-context mode is ENABLED ONLY IF:
      backend.phase == "G"
    """

    def __init__(
        self,
        model: str = "claude-sonnet-4-5",
        temperature: float = 0.2,
        max_tokens: int = 2000,
        request_timeout: Optional[float] = 120.0,
        retry_attempts: int = 5,
        api_key_env: str = "ANTHROPIC_API_KEY",
        inter_request_delay: float = 1.2,
        phase: str = "P",        # NEW: phase flag (P, F, G)
        tpm_limit: Optional[int] = None,
        enable_cache: bool = True,  # NEW: enable prompt caching
    ):
        # Phase determines whether long-context mode is activated
        self.phase = phase.upper().strip()
        self.enable_cache = enable_cache

        api_key = os.environ.get(api_key_env)
        if not api_key:
            raise ValueError(f"{api_key_env} environment variable is not set.")

        self.client = Anthropic(api_key=api_key)

        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.request_timeout = request_timeout
        self.retry_attempts = retry_attempts
        self.inter_request_delay = inter_request_delay
        self.tpm_limit = tpm_limit or 30000  # Anthropic default input TPM
        self.token_window_seconds = 60
        self._token_usage: list[tuple[float, int]] = []

        # Long-context header (only used in G-phase)
        # NOTE: Prompt caching is GA and doesn't need a beta header
        # The cache_control blocks in message content are sufficient
        self.long_context_header = {
            "anthropic-beta": "context-1m-2025-08-07"
        }

    def _estimate_prompt_tokens(self, prompt: str) -> int:
        return max(1, len(prompt) // 4)

    def _accepts_temperature(self) -> bool:
        """Whether this model still accepts the ``temperature`` parameter.

        Claude Opus 4.8 deprecated ``temperature`` at the API layer and
        returns ``400 'temperature' is deprecated for this model.`` when
        the field is present. Detect by model name so the same backend
        instance works for both Sonnet (accepts temperature) and Opus 4.8
        (rejects it).
        """
        return "opus-4-8" not in self.model

    def _throttle_for_rate_limit(self, tokens_needed: int) -> None:
        if not self.tpm_limit:
            return

        effective_tokens = min(tokens_needed, self.tpm_limit)

        while True:
            now = time.time()
            self._token_usage = [
                (ts, tok)
                for ts, tok in self._token_usage
                if now - ts < self.token_window_seconds
            ]
            used = sum(tok for _, tok in self._token_usage)
            if used + effective_tokens <= self.tpm_limit:
                return

            oldest_ts = self._token_usage[0][0] if self._token_usage else now
            wait = max(self.token_window_seconds - (now - oldest_ts), 0.0) + 0.1
            logger.info(
                "[AnthropicBackend] Throttling %.0f tokens; "
                "used=%d limit=%d sleep=%.1fs",
                effective_tokens,
                used,
                self.tpm_limit,
                wait,
            )
            time.sleep(wait)

    # ---------------------------------------------------------
    # Internal generate() method
    # ---------------------------------------------------------
    def generate(self, prompt: str) -> LLMResponse:

        est_tokens = self._estimate_prompt_tokens(prompt)
        # Include expected completion tokens to stay under TPM
        tokens_needed = est_tokens + self.max_tokens

        adaptive_delay = est_tokens / 600.0
        sleep_time = max(self.inter_request_delay, adaptive_delay)
        time.sleep(sleep_time)

        self._throttle_for_rate_limit(tokens_needed)

        last_error = None

        # Determine if long-context mode is active
        use_long_context = (self.phase == "G")
        use_cache = self.enable_cache and use_long_context

        for attempt in range(1, self.retry_attempts + 1):
            try:
                logger.info(
                    f"[AnthropicBackend] Attempt {attempt}/{self.retry_attempts} "
                    f"(long-context={use_long_context}, cache={use_cache})"
                )

                # Build message content
                if use_cache and "==== END CONTEXT ====" in prompt:
                    # Split prompt into context and instructions for caching
                    context_end_marker = "==== END CONTEXT ===="
                    split_idx = prompt.find(context_end_marker)
                    context_part = prompt[:split_idx + len(context_end_marker)]
                    instructions_part = prompt[split_idx + len(context_end_marker):]

                    content = [
                        {
                            "type": "text",
                            "text": context_part,
                            "cache_control": {"type": "ephemeral"}
                        },
                        {
                            "type": "text",
                            "text": instructions_part
                        }
                    ]
                else:
                    # Standard message (no caching)
                    content = prompt

                kwargs = {
                    "model": self.model,
                    "max_tokens": self.max_tokens,
                    "timeout": self.request_timeout,
                    "system": (
                        "You are a careful linguistic analyst. "
                        "Follow all instructions exactly. "
                        "Do not invent categories. "
                        "Report only patterns supported by data."
                    ),
                    "messages": [{"role": "user", "content": content}],
                }
                if self._accepts_temperature():
                    kwargs["temperature"] = self.temperature

                # Add headers for G-phase (long-context mode)
                # Note: Prompt caching works via cache_control blocks in content,
                # no beta header needed
                if use_long_context:
                    kwargs["extra_headers"] = self.long_context_header

                response = self.client.messages.create(**kwargs)

                # Extract text
                text_chunks = []
                for block in response.content:
                    if hasattr(block, "text"):
                        text_chunks.append(block.text)
                    elif isinstance(block, dict) and block.get("type") == "text":
                        text_chunks.append(block.get("text", ""))

                combined = "".join(text_chunks).strip()

                usage_info = getattr(response, "usage", None)
                input_tokens = None
                if usage_info is not None:
                    input_tokens = getattr(usage_info, "input_tokens", None)
                    if input_tokens is None and isinstance(usage_info, dict):
                        input_tokens = usage_info.get("input_tokens")

                actual_tokens = input_tokens or est_tokens
                capped_tokens = min(actual_tokens, self.tpm_limit) if self.tpm_limit else actual_tokens
                self._token_usage.append((time.time(), capped_tokens))

                # Extract cache usage metrics if available
                cache_creation_tokens = 0
                cache_read_tokens = 0
                if usage_info is not None:
                    cache_creation_tokens = getattr(usage_info, "cache_creation_input_tokens", 0) or 0
                    cache_read_tokens = getattr(usage_info, "cache_read_input_tokens", 0) or 0

                return LLMResponse(
                    prompt=prompt,
                    output=combined,
                    metadata={
                        "backend": "anthropic",
                        "model": self.model,
                        "temperature": (
                            self.temperature
                            if self._accepts_temperature() else None
                        ),
                        "phase": self.phase,
                        "long_context_active": use_long_context,
                        "cache_enabled": use_cache,
                        "usage": {
                            "estimated_input_tokens": est_tokens,
                            "input_tokens": input_tokens,
                            "cache_creation_input_tokens": cache_creation_tokens,
                            "cache_read_input_tokens": cache_read_tokens,
                        },
                    },
                )

            except Exception as e:
                last_error = e
                logger.warning(f"[AnthropicBackend] Error on attempt {attempt}: {e}")
                delay = max(15.0, 3.0 * attempt)
                time.sleep(delay)

        logger.error(f"[AnthropicBackend] All retries failed: {last_error}")
        raise last_error

    # Unified interface
    def complete(self, prompt: str) -> LLMResponse:
        return self.generate(prompt)

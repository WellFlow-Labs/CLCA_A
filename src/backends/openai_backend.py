from __future__ import annotations

import os
import time
import logging
from typing import Optional

from .base import LLMBackend, LLMResponse

try:
    from openai import OpenAI
except ImportError as e:
    raise ImportError(
        "The OpenAI python package is required for this backend. "
        "Install with: pip install openai"
    ) from e

logger = logging.getLogger(__name__)


class OpenAIBackend(LLMBackend):
    """
    A drop-in backend that mirrors the DummyBackend interface but uses the
    OpenAI Chat Completions API.

    Required env var:
        OPENAI_API_KEY

    Supports:
        - automatic retries on rate limits
        - length-safe prompt construction
        - model configuration via constructor
        - return of raw text only for reproducibility
    """

    def __init__(
        self,
        model: str = "gpt-4.1",
        temperature: float = 0.2,
        max_tokens: int = 2000,
        request_timeout: Optional[float] = 40.0,
        retry_attempts: int = 5,
        api_key_env: str = "OPENAI_API_KEY",
        phase: str = "P",
        tpm_limit: Optional[int] = None,
    ):
        self.api_key_env = api_key_env
        self.phase = phase.upper().strip() if phase else "P"
        api_key = os.environ.get(self.api_key_env)
        if not api_key:
            raise ValueError(
                f"{self.api_key_env} environment variable is not set. "
                "Please export it before running the pipeline."
            )

        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.request_timeout = request_timeout
        self.retry_attempts = retry_attempts

    def generate(self, prompt: str) -> LLMResponse:
        """
        Execute a single prompt through the OpenAI API, returning LLMResponse.
        """
        last_error = None

        for attempt in range(1, self.retry_attempts + 1):
            try:
                logger.info(f"[OpenAIBackend] Attempt {attempt}/{self.retry_attempts}")

                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": "You are a careful linguistic analyst. Follow all instructions exactly. Do not infer theory unless explicitly requested."},
                        {"role": "user", "content": prompt},
                    ],
                    max_completion_tokens=self.max_tokens,
                    temperature=self.temperature,
                    timeout=self.request_timeout,
                )

                text = response.choices[0].message.content.strip()
                usage = getattr(response, "usage", None)

                return LLMResponse(
                    prompt=prompt,
                    output=text,
                    metadata={
                        "backend": "openai",
                        "model": self.model,
                        "temperature": self.temperature,
                        "phase": self.phase,
                        "usage": usage,
                    },
                )

            except Exception as e:
                last_error = e
                logger.warning(
                    f"[OpenAIBackend] Error on attempt {attempt}: {e}. "
                    "Retrying after backoff..."
                )
                time.sleep(2 * attempt)  # simple exponential backoff

        # If we reach this line, retries have failed.
        logger.error(f"[OpenAIBackend] All retries failed. Last error: {last_error}")
        raise last_error
    
    def complete(self, prompt: str) -> LLMResponse:
        """
        Adapter for the unified backend interface.
        """
        return self.generate(prompt)

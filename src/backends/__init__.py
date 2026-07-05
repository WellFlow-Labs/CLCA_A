from __future__ import annotations

from typing import Any

from .dummy_backend import DummyBackend

try:  # Optional dependency
    from .openai_backend import OpenAIBackend
except Exception:
    OpenAIBackend = None

try:  # Optional dependency
    from .anthropic_backend import AnthropicBackend
except Exception:
    AnthropicBackend = None


def _extract_backend_config(settings_or_name: Any):
    """
    Accepts either a Settings dataclass or a plain backend name and returns
    the normalized backend name plus kwargs for the concrete backend.
    """
    if hasattr(settings_or_name, "backend"):
        name = getattr(settings_or_name, "backend")
        kwargs = {
            "model": getattr(settings_or_name, "model_name", None),
            "temperature": getattr(settings_or_name, "temperature", None),
            "max_tokens": getattr(settings_or_name, "max_tokens", None),
            "api_key_env": getattr(settings_or_name, "api_key_env", None),
            "phase": getattr(settings_or_name, "phase", None),
            "tpm_limit": getattr(settings_or_name, "tpm_limit", None),
            "request_timeout": getattr(settings_or_name, "request_timeout", None),
            "request_delay": getattr(settings_or_name, "request_delay", None),
        }
    else:
        name = str(settings_or_name)
        kwargs = {}

    # Remove None values so backends fall back to their defaults
    kwargs = {k: v for k, v in kwargs.items() if v is not None}
    return name.lower(), kwargs


def get_backend(settings_or_name: Any):
    name, kwargs = _extract_backend_config(settings_or_name)
    request_delay = kwargs.pop("request_delay", None)

    if name == "dummy":
        return DummyBackend()

    if name == "openai":
        if OpenAIBackend is None:
            raise RuntimeError("OpenAI backend unavailable (missing dependency).")
        return OpenAIBackend(**kwargs)

    if name == "anthropic":
        if AnthropicBackend is None:
            raise RuntimeError("Anthropic backend unavailable (missing dependency).")
        if request_delay is not None and "inter_request_delay" not in kwargs:
            kwargs["inter_request_delay"] = request_delay
        return AnthropicBackend(**kwargs)

    raise ValueError(f"Unknown backend: {name}")

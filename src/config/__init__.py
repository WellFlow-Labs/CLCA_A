from __future__ import annotations

from dataclasses import dataclass, asdict, fields
from pathlib import Path
from typing import Any, Optional

import tomllib


_BASE_DIR = Path(__file__).resolve().parent


@dataclass
class Settings:
    """
    Simple settings holder.

    Defaults are sane but can be overridden via settings.toml and/or
    constructor / with_overrides().
    """
    backend: str = "openai"
    model_name: str = "gpt-4.1"
    temperature: float = 0.2
    max_tokens: int = 2000
    tpm_limit: Optional[int] = None
    retry_attempts: int = 5
    request_timeout: Optional[float] = None

    # Current pipeline phase (P, I, F, G)
    phase: str = "P"

    # Which env var to read the key from (e.g. OPENAI_API_KEY / ANTHROPIC_API_KEY)
    api_key_env: Optional[str] = None

    # Optional delay (in seconds) between calls – used for rate-limit smoothing.
    request_delay: float = 0.0

    @classmethod
    def from_file(cls, path: Optional[Path] = None) -> "Settings":
        """
        Load defaults from settings.toml if present, else fall back to hard-coded defaults.
        """
        if path is None:
            path = _BASE_DIR / "settings.toml"

        if not path.exists():
            return cls()

        with path.open("rb") as f:
            data = tomllib.load(f)

        # Backwards compat: "model" -> "model_name"
        if "model" in data and "model_name" not in data:
            data["model_name"] = data.pop("model")

        # Filter to only known Settings fields (ignore nested tables like
        # [phase.*], [step_overrides], and unknown keys like api_mode)
        known = {f.name for f in fields(cls)}
        filtered = {k: v for k, v in data.items() if k in known}

        return cls(**filtered)

    def with_overrides(self, **overrides: Any) -> "Settings":
        """
        Return a new Settings with the given keyword overrides applied (ignoring None).
        """
        base = asdict(self)
        for k, v in overrides.items():
            if v is not None:
                base[k] = v
        return Settings(**base)

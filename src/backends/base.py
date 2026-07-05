from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class LLMResponse:
    prompt: str
    output: str
    metadata: dict[str, Any] | None = None


class LLMBackend(ABC):
    """
    Abstract interface for pluggable LLM backends.
    """

    @abstractmethod
    def generate(self, prompt: str) -> LLMResponse:
        """
        Execute a single prompt and return the response.
        """
        raise NotImplementedError

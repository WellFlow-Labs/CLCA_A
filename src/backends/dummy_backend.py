from __future__ import annotations

from dataclasses import dataclass

from .base import LLMBackend, LLMResponse


@dataclass
class DummyBackend(LLMBackend):
    """
    A no-op backend for testing.

    It simply echoes the prompt with a banner so you can test file IO and
    pipeline behavior without burning tokens.
    """

    def generate(self, prompt: str) -> LLMResponse:
        banner = (
            "DUMMY BACKEND OUTPUT\n"
            "--------------------\n"
            "This is a placeholder. Integrate a real backend (e.g., OpenAI) "
            "when you're ready.\n\n"
        )
        return LLMResponse(
            prompt=prompt,
            output=banner + prompt,
            metadata={"backend": "dummy", "model": "dummy"},
        )

    def complete(self, prompt: str) -> LLMResponse:
        """
        Adapter for compatibility with newer runner code.
        """
        return self.generate(prompt)

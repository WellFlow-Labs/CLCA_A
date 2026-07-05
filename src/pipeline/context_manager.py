import json
from pathlib import Path
from typing import List, Dict


class ContextManager:
    """
    Stores and retrieves CLCA context consisting of all previous
    step outputs in chronological order.

    The context file format is JSONL:

        {"step": "P1_vocab", "prompt": "...", "output": "..."}
        {"step": "P2_derivations", "prompt": "...", "output": "..."}
        ...

    NOTE: When *providing* context to prompts, we now only return
    the OUTPUT text, never the prompt text, to keep token size small
    and avoid polluting the linguistic signal.
    """

    CONTEXT_FILE = "context.jsonl"

    def __init__(self, base_output_dir: Path):
        self.context_path = base_output_dir / self.CONTEXT_FILE
        self.context_path.touch(exist_ok=True)

    # ------------------------------------------------------------
    # Load full JSONL history as a list of dicts
    # ------------------------------------------------------------
    def load_history(self) -> List[Dict]:
        if not self.context_path.exists():
            return []

        text = self.context_path.read_text(encoding="utf-8")
        if not text.strip():
            return []

        history: List[Dict] = []
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                history.append(json.loads(line))
            except json.JSONDecodeError:
                # Skip any corrupted lines but continue
                continue
        return history

    # ------------------------------------------------------------
    # Return *all* previous outputs as a single block (rarely used now)
    # (Still output-only, no prompts.)
    # ------------------------------------------------------------
    def gather_context(self) -> str:
        history = self.load_history()
        blocks: List[str] = []

        for entry in history:
            step = entry.get("step", "")
            output = entry.get("output", "")

            blocks.append(
                f"\n\n### STEP {step} — OUTPUT\n{output}\n"
            )

        return "".join(blocks)

    # ------------------------------------------------------------
    # Return only the outputs for a specific subset of steps
    # (according to dependencies.toml)
    # ------------------------------------------------------------
    def gather_subset(self, required_steps: List[str]) -> str:
        """
        Build a context string containing ONLY the outputs for the
        given step codes, in the order they originally ran.

        - Does NOT include any prompt text.
        - Skips any unknown / missing steps silently.
        """
        if not required_steps:
            return ""

        required_set = set(required_steps)
        history = self.load_history()
        blocks: List[str] = []

        for entry in history:
            step = entry.get("step", "")
            if step not in required_set:
                continue

            output = entry.get("output", "")
            blocks.append(
                f"\n\n### STEP {step} — OUTPUT\n{output}\n"
            )

        return "".join(blocks)

    # ------------------------------------------------------------
    # Append the latest step (prompt + output) to the JSONL log
    # ------------------------------------------------------------
    def append_step_output(self, step: str, prompt: str, output: str) -> None:
        entry = {
            "step": step,
            "prompt": prompt,
            "output": output,
        }
        with self.context_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")



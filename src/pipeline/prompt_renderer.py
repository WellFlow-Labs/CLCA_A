from jinja2 import Environment, StrictUndefined, BaseLoader

class PromptRenderer:
    """
    Renders Jinja2 templates for CLCA prompts with:
    - strict undefined variable handling
    - deterministic whitespace control
    - standard metadata (language info + context + settings)
    """

    def __init__(self, settings, lang_info: dict, output_dir):
        self.settings = settings
        self.lang_info = lang_info
        self.output_dir = output_dir

        self.env = Environment(
            loader=BaseLoader(),
            undefined=StrictUndefined,
            autoescape=False,
            trim_blocks=True,
            lstrip_blocks=True,
        )

    # ------------------------------------------------------------
    # MUST MATCH run_language.py CALL SIGNATURE
    # ------------------------------------------------------------
    def render(self, template_text: str, context: str) -> str:
        """
        Render a single CLCA prompt with full cumulative context.
        """

        template = self.env.from_string(template_text)

        rendered = template.render(
            language=self.lang_info,
            lang=self.lang_info,        # support legacy variable name
            context=context,
            settings=self.settings
        )

        # Optional cleanup to remove trailing spaces and normalize
        cleaned = "\n".join(line.rstrip() for line in rendered.splitlines())
        return cleaned + "\n"

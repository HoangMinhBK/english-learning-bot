import google.generativeai as genai

from oslo_config import cfg

CONF = cfg.CONF
genai.configure(api_key=CONF.gemini.GOOGLE_API_KEY)


class GeminiHighLight:
    def __init__(self) -> None:
        self.google_api_key = CONF.gemini.GOOGLE_API_KEY
        self.generative_module = CONF.gemini.GOOGLE_GENERATIVE_MODULE
        self.command = CONF.gemini.GOOGLE_PROMPT_COMMAND
        self.model = genai.GenerativeModel(self.generative_module)

    def generate_summary_from_url(self, url) -> str:
        prompt_query = f"Summary this url with about 15 sentences for url: {url}"
        response = self.model.generate_content(prompt_query)
        return response.text

    def generate_highlight_from_summary(self, summary):
        prompt_query = f"{self.command} for {summary}"

        response = self.model.generate_content(prompt_query)

        return response.text

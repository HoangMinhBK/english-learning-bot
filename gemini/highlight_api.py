import google.generativeai as genai

from config.settings import Settings

genai.configure(api_key=Settings.GOOGLE_API_KEY)


class GeminiHighLight:
    def __init__(self) -> None:
        self.google_api_key = Settings.GOOGLE_API_KEY
        self.generative_module = Settings.GOOGLE_GENERATIVE_MODULE
        self.command = Settings.GOOGLE_PROMPT_COMMAND
        self.model = genai.GenerativeModel(self.generative_module)

    def generate_highlight_from_summary(self, summary):
        prompt_query = f"{self.command} for {summary}"

        response = self.model.generate_content(prompt_query)

        return response.text

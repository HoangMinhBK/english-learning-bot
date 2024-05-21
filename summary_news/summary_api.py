import requests

from config.settings import Settings
from utils.contants import DEFAULT_NUMBER_OF_SENTENCES_SUMMARY


class SummaryApi:
    def __init__(self) -> None:
        self.url = Settings.SUMMARY_API_URL
        self.api_key = Settings.SUMMARY_API_KEY
        self.api_host = Settings.SUMMARY_API_HOST
        self.headers = {
            "Accept": "application/json",
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": self.api_host,
        }

    def get_summary(self, url=None, text=None) -> str:
        params = {"sentences": DEFAULT_NUMBER_OF_SENTENCES_SUMMARY}
        if url:
            params["url"] = url
        elif text:
            params["text"] = text
        else:
            raise ValueError("Both url and text cannot be null!")

        response = requests.get(url=self.url, params=params, headers=self.headers)

        if response.ok:
            summary = response.json().get("summary", "")
            return summary
        else:
            raise ValueError(
                f"Get summary fail with status code {response.status_code} and text {response.text}"
            )

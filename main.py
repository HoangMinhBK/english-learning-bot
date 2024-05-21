import nltk
from telegram import Bot

from config.settings import Settings
from gemini.highlight_api import GeminiHighLight
from news.news_api import NewsAPI
from summary_news.summary_api import SummaryApi
from utils.nltk_utils import NLTKUtils

BOT_TOKEN = Settings.TELEGRAM_TOKEN
chat_id = Settings.TARGET_CHAT_ID
NEW_API_KEY = Settings.NEWS_API_KEY
GOOGLE_API_KEY = Settings.GOOGLE_API_KEY
bot = Bot(token=BOT_TOKEN)

# Download NLTK resources (required for WordNet)
nltk.download("punkt")
nltk.download("wordnet")


def send_news():
    summaries = NewsAPI.get_news_summary(NEW_API_KEY)

    for title, description, url in summaries:
        # Send the news title and URL
        title_message = f"[{title}]({url})"
        # summary_agent = SummaryApi()
        highlight_agent = GeminiHighLight()
        # summary = summary_agent.get_summary(url=url)
        summary = "For the original television series, see Star Trek: The Original Series. Star Trek is an American media franchise based on the science fiction television series created by Gene Roddenberry. The Star Trek canon of the franchise includes The Original Series, an animated series, five spin-off television series, the film franchise, and further adaptations in several media. In creating Star Trek, Roddenberry was inspired by the Horatio Hornblower novels, the satirical book Gulliver's Travels, and by works of western genre such as the television series Wagon Train. Four spin-off television series were eventually produced: Star Trek: The Next Generation followed the crew of a new starship Enterprise set a century after the original series; Star Trek: Deep Space Nine and Star Trek: Voyager set contemporaneously with The Next Generation; and Star Trek: Enterprise set before the original series in the early days of human interstellar travel."
        high_light = highlight_agent.generate_highlight_from_summary(summary=summary)

        # with title, summary and highlight, send to target chat id

        bot.send_message(chat_id=chat_id, text=title_message, parse_mode="Markdown")
        bot.send_message(
            chat_id=chat_id,
            text=NLTKUtils.escape_markdown(summary),
            parse_mode="Markdown",
        )
        bot.send_message(
            chat_id=chat_id,
            text=NLTKUtils.escape_markdown(high_light),
            parse_mode="Markdown",
        )

        # Send the news description in chunks
        # for chunk in chunks(
        #     description, 4000
        # ):  # Split description into chunks of max 4000 characters
        #     escaped_chunk = NLTKUtils.escape_markdown(chunk)
        #     bot.send_message(
        #         chat_id=chat_id,
        #         text=escaped_chunk,
        #         parse_mode="Markdown",
        #     )

        # Send the highlighted words and their meanings
        # highlighted_text, word_details = NLTKUtils.highlight_and_define_words(
        #     description
        # )
        # details_message = "Highlighted words and their meanings:\n\n"
        # for word, meanings in word_details.items():
        #     # Extract relevant information from meanings and concatenate into details_message
        #     meanings_str = "\n".join(
        #         [
        #             f"- Definition: {meaning['definition']}\n"
        #             f"  Synonyms: {meaning['synonyms']}\n"
        #             f"  Example: {meaning['example']}\n"
        #             f"  Pronunciation: {meaning['pronunciation']}"
        #             for meaning in meanings
        #         ]
        #     )
        #     details_message += f"*{word}*\n{meanings_str}\n\n"

        # # Send the details message in chunks
        # for chunk in chunks(details_message, 4000):
        #     escaped_chunk = NLTKUtils.escape_markdown(chunk)
        #     bot.send_message(
        #         chat_id=chat_id,
        #         text=escaped_chunk,
        #         parse_mode="Markdown",
        #     )


def chunks(text, chunk_size):
    """Split text into chunks of specified size"""
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]


if __name__ == "__main__":
    send_news()

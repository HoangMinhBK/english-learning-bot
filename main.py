import nltk
from telegram import Bot
from config.settings import Settings
from news.news_api import NewsAPI
from utils.nltk_utils import NLTKUtils

bot = Bot(token=Settings.TELEGRAM_TOKEN)

# Download NLTK resources (required for WordNet)
nltk.download("punkt")
nltk.download("wordnet")


def send_news():
    summaries = NewsAPI.get_news_summary(Settings.NEWS_API_KEY)

    for title, description, url in summaries:
        # Send the news title and URL
        title_message = f"[{title}]({url})"
        bot.send_message(
            chat_id=Settings.TARGET_CHAT_ID, text=title_message, parse_mode="Markdown"
        )

        # Send the news description in chunks
        for chunk in chunks(
            description, 4000
        ):  # Split description into chunks of max 4000 characters
            escaped_chunk = NLTKUtils.escape_markdown(chunk)
            bot.send_message(
                chat_id=Settings.TARGET_CHAT_ID,
                text=escaped_chunk,
                parse_mode="Markdown",
            )

        # Send the highlighted words and their meanings
        highlighted_text, word_details = NLTKUtils.highlight_and_define_words(
            description
        )
        details_message = "Highlighted words and their meanings:\n\n"
        for word, meanings in word_details.items():
            # Extract relevant information from meanings and concatenate into details_message
            meanings_str = "\n".join(
                [
                    f"- Definition: {meaning['definition']}\n  Synonyms: {meaning['synonyms']}\n  Example: {meaning['example']}\n  Pronunciation: {meaning['pronunciation']}"
                    for meaning in meanings
                ]
            )
            details_message += f"*{word}*\n{meanings_str}\n\n"

        # Send the details message in chunks
        for chunk in chunks(details_message, 4000):
            escaped_chunk = NLTKUtils.escape_markdown(chunk)
            bot.send_message(
                chat_id=Settings.TARGET_CHAT_ID,
                text=escaped_chunk,
                parse_mode="Markdown",
            )


def chunks(text, chunk_size):
    """Split text into chunks of specified size"""
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]


if __name__ == "__main__":
    send_news()

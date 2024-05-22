from oslo_config import cfg
from telegram import Bot
from gemini.highlight_api import GeminiHighLight
from news.news_api import NewsAPI
from utils.nltk_utils import NLTKUtils

CONF = cfg.CONF
BOT_TOKEN = CONF.bot_telegram.TELEGRAM_BOT_TOKEN
bot = Bot(token=BOT_TOKEN)
chat_ids = CONF.bot_telegram.TARGET_CHAT_IDS

def send_news():
    summaries = NewsAPI.get_news_summary(CONF.news_api.NEWS_API_KEY)
    for title, description, url in summaries:
        # Send the news title and URL
        title_message = f"[{title}]({url})"
        # summary_agent = SummaryApi()
        generative_agent = GeminiHighLight()
        summary = generative_agent.generate_summary_from_url(url=url)
        high_light = generative_agent.generate_highlight_from_summary(summary=summary)

        for chat_id in chat_ids:
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

from oslo_config import cfg

bot_telegram_opts = [
    cfg.StrOpt("TELEGRAM_BOT_TOKEN", default=""),
    cfg.ListOpt("TARGET_CHAT_IDS", default=""),
]

bot_telegram_groups = cfg.OptGroup(name='bot_telegram', title='bot_telegram')

def register_opts(conf):
    conf.register_group(bot_telegram_groups)
    conf.register_opts(bot_telegram_opts, bot_telegram_groups)


def list_opts():
    return bot_telegram_groups, bot_telegram_opts
from oslo_config import cfg

news_api_opts = [
    cfg.StrOpt("NEWS_API_KEY", default=""),
]

news_api_groups = cfg.OptGroup(name='news_api', title='news_api')

def register_opts(conf):
    conf.register_group(news_api_groups)
    conf.register_opts(news_api_opts, news_api_groups)


def list_opts():
    return news_api_groups, news_api_opts
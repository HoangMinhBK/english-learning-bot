from oslo_config import cfg

gemini_groups = cfg.OptGroup(name='gemini', title='gemini')

gemini_opts = [
    cfg.StrOpt("GOOGLE_API_KEY", default=""),
    cfg.StrOpt("GOOGLE_GENERATIVE_MODULE", default="gemini-1.0-flash-latest"),
    cfg.StrOpt("GOOGLE_PROMPT_COMMAND", default="Show highlights and definition, usage"),
]

def register_opts(conf):
    conf.register_group(gemini_groups)
    conf.register_opts(gemini_opts, gemini_groups)


def list_opts():
    return gemini_groups, gemini_opts
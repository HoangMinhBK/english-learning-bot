import sys
import nltk
import config

CONF = config.CONF
#from messages import send_news

# Download NLTK resources (required for WordNet)
nltk.download("punkt")
nltk.download("wordnet")


def parse_args(argv = None):
    argv = (argv if argv is not None else sys.argv[1:])
    args = argv or []
    CONF(args=args,
         prog=sys.argv[1:],
         project='english-learning-bot',
         version="1.0",
         default_config_files='config.conf',
         description='English learning bot.')
    config.register_opts()


def chunks(text, chunk_size):
    """Split text into chunks of specified size"""
    return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]


if __name__ == "__main__":
    parse_args()
    from messages import send_news
    send_news()

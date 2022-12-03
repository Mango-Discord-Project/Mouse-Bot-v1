from urllib.parse import (urlparse, parse_qsl, ParseResult)

# ============================================
# parsers
# ============================================

def parser_base(parser: ParseResult) -> dict:
    """Sample of Parsers"""
    ...

def twitter(parser: ParseResult) -> dict:
    user_id = parser.path.split('/')[1]
    tweet_id = 
    

def pixiv(parser: ParseResult) -> dict:
    ...

# ============================================
# mappings
# ============================================

url_map = {
    "twitter.com": twitter,
    "pixiv.com": pixiv
}

url_translate_map = {
    "twitter.com": [
        "m.twitter.com",
        "mobile.twitter.com"
    ]
}

# ============================================
# functions
# ============================================

def url_translator(netloc: str):
    if netloc.startswith('www.'):
        netloc = netloc.removeprefix('www.')
    for key, value in url_translate_map.items():
        if netloc in value:
            return key
    return netloc

false = lambda *args, **kwargs: False

def url_parser(url: str) -> object:
    parser = urlparse(url)
    parser.netloc = url_translator(parser.netloc)
    parser.query = parse_qsl(parser.query)
    return url_map.get(parser.netloc, false)(parser)
import json

__all__ = [
    'get_bot_config'
]

def get_bot_config():
    with open('./config/bot_setting.json', encoding='utf8') as file:
        return json.load(file)
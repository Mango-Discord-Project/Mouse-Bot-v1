from os import path, listdir
from typing import Iterable
import json

_config_path = '.', 'src', 'v2.0', 'config', 'command', 'config.json'
_default_config_path = '.', 'src', 'v2.0', 'config', 'command', 'default.json'
_localization_path = '.', 'src', 'v2.0', 'config', 'localization'

config_path = path.join(*_config_path)
default_path = path.join(*_default_config_path)
localization_path = path.join(*_localization_path)

with open(default_path) as file:
    default_data = json.load(file)

def _command_config(_key: str, use_default: bool = True) -> dict:
    with open(config_path) as file:
        data = json.load(file)
    if not use_default:
        return data.get(_key, {})
    return default_data | data.get(_key, {})

def _localization(_key: str) -> dict:
    data = {'name_localizations': {}, 'description_localizations': {}}
    
    for filename in listdir(localization_path):
        with open(path.join(localization_path, filename), encoding='utf8') as file:
            json_data = json.load(file)
            for key in ('name', 'description'):
                value = json_data.get(f'{_key}.{key}', False)
                if value:
                    data[f'{key}_localizations'][filename.removesuffix('.json')] = value
    
    for key, value in data.copy().items():
        if not value:
            del data[key]
    
    return data

def mixin(_key: str = None, use_default: bool = True) -> dict:
    if _key is None:
        return default_data
    return _command_config(_key, use_default) | _localization(_key)

def generate_mixin(keys: Iterable[str]) -> dict:
    return {k: mixin(k) for k in keys}

__all__ = ['mixin', 'generate_mixin']
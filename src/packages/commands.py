import os
import json

i18n_file_path, info_file_path = './config/localization/', './config/command_info.json'

def i18n_mixin(command_id: str) -> dict:
    langs = {"name_localizations": {}, "description_localizations": {}}

    for lang in os.listdir(i18n_file_path):
        with open(i18n_file_path + lang, encoding='utf8') as file:
            data = json.load(file)

        for langs_key, file_key in (('name_localizations', 'name'), ('description_localizations', 'description')):
            if lang_data:=data.get(f'command.{command_id}.{file_key}'):
                langs[langs_key][lang.split('.')[0]] = lang_data

    return langs

def command_argument_mixin(command_id: str) -> dict:
    with open(info_file_path, encoding='utf8') as info_file:
        info = json.load(info_file).get(command_id, {})

    return info | i18n_mixin(command_id)
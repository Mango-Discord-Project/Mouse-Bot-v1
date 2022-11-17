import os
import json
# import tomllib

import discord
from discord import ApplicationContext
import dotenv
from rich.console import Console

global_console = Console()
global_console.log('GLOBAL > Start')

class Bot(discord.Bot):
    def __init__(self):
        super().__init__()
        self.console = Console()
        self._add_command()
    
    def i18n_mixin(self, command_id: str) -> dict:
        langs = {"name_localizations": {}, "description_localizations": {}}
        for lang in os.listdir('./config/localization/'):
            with open(f'./config/localization/{lang}', encoding='utf8') as file:
                data = json.load(file)
            for langs_key, file_key in (('name_localizations', 'name'), ('description_localizations', 'description')):
                if lang_data:=data.get(f'command.{command_id}.{file_key}'):
                    langs[langs_key][lang.split('.')[0]] = lang_data
        # self.console.print(langs)
        return langs
    
    def command_argument_mixin(self, command_id: str) -> dict:
        with open('./config/command_info.json') as info_file:
            info = json.load(info_file).get(command_id, {})
        return info | self.i18n_mixin(command_id)

    def _add_command(self):
        @self.slash_command(**self.command_argument_mixin('main.ping'))
        async def ping(ctx: ApplicationContext):
            await ctx.respond(f'{self.latency*1000:.4f}')

    async def on_ready(self):

        self.console.log('.MAIN > Bot is on Ready')
if __name__ == '__main__':
    dotenv.load_dotenv()
    bot = Bot()
    bot.run(os.getenv('TOKEN'))

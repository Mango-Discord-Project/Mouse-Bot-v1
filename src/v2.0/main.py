import json
from os import path, listdir, getenv
from typing import Self

from discord import Bot as discord_bot
from discord import ApplicationContext, Option, Intents
import pretty_errors
import dotenv
from rich import console

from packages import *

g_console = Logger(logger_prefix='GLOBAL')
g_console.log('Start')

class Bot(discord_bot, LoggerBot):
    def __init__(self: Self):
        super().__init__(intents=Intents.all())
        
        # logger
        self.console = console.Console()
        self.logger_prefix = 'MAIN'
        
        # set attribute
        self._add_command()
        with open(path.join('.', 'src', 'v2.0', 'config', 'bot', 'attributes.json'), encoding='utf8') as file:
            self.__dict__ |= json.load(file)
        
        # load cogs
        cogs_path = path.join(*self.cogs_path)
        self.load_extensions(*(f'cogs.{i.removesuffix(".py")}' for i in listdir(cogs_path) if i.endswith('.py')))

    def _add_command(self: Self):
        @self.slash_command(**mixin())
        async def ping(ctx: ApplicationContext):
            self.log(f'{ctx.author} use {ctx.command.qualified_name}')
            await ctx.respond(f'ping: `{self.latency*1000:.4f}`')
        
        @self.slash_command(**mixin())
        async def cog(ctx: ApplicationContext, 
                      cog_name: Option(str, 'the name of the cog', required=True),
                      action: Option(str, choices=['load', 'reload', 'unload'], required=False, default='reload')):
            if ctx.author.id not in self.author_ids:
                return await ctx.respond(f'You are not Mouse Bot\' developer')
            getattr(self, f'{action}_extension')(f'cogs.{cog_name}')
            await ctx.respond(f'Success {action} {cog_name}', ephemeral=True)

    async def on_ready(self):
        self.log('Bot is on Ready')


if __name__ == '__main__':
    g_console.log('Loading .env')
    dotenv.load_dotenv()
    
    g_console.log('Building Bot Object')
    bot = Bot()
    
    g_console.log('Bot Start Running')
    bot.run(getenv('TOKEN'))
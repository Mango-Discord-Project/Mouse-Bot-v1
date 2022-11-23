import os
import json
# import tomllib

import discord
from discord import ApplicationContext
import dotenv
from rich.console import Console

from packages import *

global_console = Logger(prefix='GLOBAL > ')
global_console.log('Start')

class Bot(discord.Bot):
    def __init__(self):
        super().__init__()
        self.console = Logger(prefix='.MAIN > ')
        self._add_command()

    def _add_command(self):
        @self.slash_command(**command_argument_mixin('main.ping'))
        async def ping(ctx: ApplicationContext):
            self.console.log(f'{ctx.author} use {ctx.command.qualified_name}')
            await ctx.respond(f'{self.latency*1000:.4f}')

    async def on_ready(self):
        self.console.log('Bot is on Ready')

        self.load_extension('cogs.url_utils')
        # extensions = [f'cogs.{file[:-3]}' for file in os.listdir('./cogs') if file.endswith('.py')]
        # error = self.load_extensions(*extensions,)
        # if error:
        #     self.console.log(error)


if __name__ == '__main__':
    global_console.log('Loading .env')
    dotenv.load_dotenv()
    
    global_console.log('Building Bot Object')
    bot = Bot()
    
    global_console.log('Bot Start Running')
    bot.run(os.getenv('TOKEN'))

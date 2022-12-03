import os
from typing import Self

from discord import Bot as discord_bot
from discord import ApplicationContext, Option, Intents
import dotenv

from packages import *

global_console = Logger(prefix='GLOBAL > ')
global_console.log('Start')

class Bot(discord_bot):
    def __init__(self: Self):
        super().__init__(intents=Intents.all())
        self.console = Logger(prefix='.MAIN > ')
        self._add_command()
        self.__dict__ |= get_bot_config()
        
        # load cogs
        self.load_extensions(*(f'cogs.{i.removesuffix(".py")}' for i in os.listdir('./cogs') if i.endswith('.py')))

    def _add_command(self: Self):
        @self.slash_command(**command_argument_mixin('main.ping'))
        async def ping(ctx: ApplicationContext):
            self.console.log(f'{ctx.author} use {ctx.command.qualified_name}')
            await ctx.respond(f'ping: `{self.latency*1000:.4f}`')
        
        @self.slash_command(**command_argument_mixin('main.cog'))
        async def cog(ctx: ApplicationContext, 
                      cog_name: Option(str, 'the name of the cog', required=True),
                      action: Option(str, choices=['load', 'reload', 'unload'], required=False, default='reload')):
            if ctx.author.id not in self.author_ids:
                return ctx.respond(f'You are not Mouse Bot\' developer')
            getattr(self, f'{action}_extension')(f'cogs.{cog_name}')
            await ctx.respond(f'Success {action} {cog_name}', ephemeral=True)

    async def on_ready(self):
        self.console.log('Bot is on Ready')


if __name__ == '__main__':
    global_console.log('Loading .env')
    dotenv.load_dotenv()
    
    global_console.log('Building Bot Object')
    bot = Bot()
    
    global_console.log('Bot Start Running')
    bot.run(os.getenv('TOKEN'))
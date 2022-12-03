from discord import Bot, ApplicationContext, commands
from discord.ext.commands import Cog
from discord.ext import tasks
from packages import *

class MainLoop(Cog):
    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot: Bot = bot
        self.console = Logger(prefix='MainLoop > ')
        self.console.log('Load Cog Success')
    
    @tasks.loop(hours=1)
    async def mixin_config_save(self):
        ...
        # with open('./config/mixin_config.json', 'w', encoding='utf8') as file:

def setup(bot: Bot) -> None:
    bot.add_cog(MainLoop(bot))
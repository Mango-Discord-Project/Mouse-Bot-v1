from discord import Bot, ApplicationContext
from discord.commands import slash_command
from discord.ext.commands import Cog
# from packages import *

class URL_Utils(Cog):

    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot: Bot = bot
        self.console = Logger(prefix='URL_Utils > ')
        self.console.log('Load Cog Success')

    @slash_command(guild_ids=[961237448552218675],name='test')
    async def test(self, ctx: ApplicationContext):
        await ctx.respond('TEST')

def setup(bot: Bot) -> None:
    bot.add_cog(URL_Utils(bot))
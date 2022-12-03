from discord import Bot, ApplicationContext, commands, SlashCommandGroup, Option
from discord.ext.commands import Cog
from packages import *

class Test(Cog):
    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot: Bot = bot
        self.console = Logger(prefix='Test > ')
        self.console.log('Load Cog Success')
    
    test_group = SlashCommandGroup('test_group', 'for developer test', guild_ids=[961237448552218675])

    @commands.slash_command(guild_ids=[961237448552218675])
    async def test(self, ctx: ApplicationContext):
        await ctx.respond('TEST')
    
    @test_group.command()
    async def test_2(self, ctx: ApplicationContext, arg: Option(str)):
        await ctx.respond(arg)

def setup(bot: Bot) -> None:
    bot.add_cog(Test(bot))
from discord import Bot, ApplicationContext, commands, SlashCommandGroup, Option, Message
from discord.ext.commands import Cog
from packages import *
import pretty_errors

def private_message_check(ctx: ApplicationContext):
    return [ctx.author.guild_permissions.administrator]

class Test(Cog, LoggerCog):
    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot: Bot = bot
        self.logger_prefix = 'Test'
        self.log('Load Cog Success')
    
    test_group = SlashCommandGroup('test_group', 'for developer test', guild_ids=[961237448552218675])

    @commands.slash_command(guild_ids=[961237448552218675])
    async def test(self, ctx: ApplicationContext):
        await ctx.respond('TEST')
    
    @test_group.command()
    async def test_2(self, ctx: ApplicationContext, arg: Option(str)):
        await ctx.respond(arg)
    
    @commands.slash_command(guild_ids=[849569027235250186])
    async def private(self, ctx: ApplicationContext):
        await ctx.respond('Private Respond', ephemeral=True)
        await ctx.channel.send('Public Respond')
    
    # @commands.message_command(checks=private_message_check, **mixin())
    # async def private_message(self, ctx: ApplicationContext, message: Message):
    #     await ctx.respond('do')

def setup(bot: Bot) -> None:
    bot.add_cog(Test(bot))
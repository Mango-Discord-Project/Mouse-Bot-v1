from datetime import datetime
from typing import Self

from discord import Bot, SlashCommandGroup, Message, ApplicationContext, Embed, Option
from discord.commands import message_command
from discord.ext.commands import Cog
from packages import *

class Homo(Cog, LoggerCog):
    def __init__(self: Self, bot: Bot) -> None:
        super().__init__()
        self.bot: Bot = bot
        self.logger_prefix = 'Homo'
        self.log('Load Cog Success')
    
    homo = SlashCommandGroup('homo', **mixin('default.homo', True))
    
    @message_command(**mixin('default.homo', True))
    async def good_sentence(self: Self, ctx: ApplicationContext, message: Message):
        if not message.content:
            return await ctx.respond('Textless messages are not supported', ephemeral=True)
        channel = self.bot.get_channel(1038818486564163704)
        if channel is None:
            return await ctx.respond('Can\'t find #good-sentences channel', ephemeral=True)
        await ctx.respond(f'Already send to {channel.mention}', ephemeral=True)
        embed = Embed(title='Good Sentence', description=message.content, color=0x2f3136)
        embed.set_author(name=message.author, icon_url=message.author.avatar.url)
        embed.set_footer(text=datetime.strftime(message.created_at, r'%c'))
        await channel.send(embed=embed)
    
    @homo.command()
    async def fuck(self: Self, ctx: ApplicationContext, 
                   message: Option(str, description='Fuck you, fuck me, fuck everything', required=True),
                   is_private: Option(str, choices=['Yes', 'No'], required=False, default='No')):
        
        channel = self.bot.get_channel(1023839492601282634)
        if channel is None:
            return await ctx.respond('Can\'t find #fuck-everything channel', ephemeral=True)
        
        embed = Embed(title='Fuck you, fuck me, fuck everything', description=message.replace('\\n', '\n'), color=0x2f3136)
        embed.set_footer(text=datetime.strftime(datetime.now(), r'%c'))
        if is_private == 'No':
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar.url)
        await channel.send(embed=embed)
        await ctx.respond(f'Already send to {channel.mention}', ephemeral=True)

def setup(bot: Bot) -> None:
    bot.add_cog(Homo(bot))
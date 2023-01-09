from datetime import datetime
from typing import Self
from uuid import uuid4

from discord import Bot, SlashCommandGroup, Message, ApplicationContext, Embed, commands, Role, VoiceChannel, StageChannel
from discord.ext.commands import Cog
from discord import errors
from packages import *



class HentaiBus(Cog, LoggerCog):
    def __init__(self: Self, bot: Bot) -> None:
        super().__init__()
        self.bot: Bot = bot
        self.logger_prefix = 'HentaiBus'
        self.log('Load Cog Success')
    
    hentai_bus = SlashCommandGroup('hentai_bus', **mixin('default.hentai_bus', True))
    
    @commands.message_command(**mixin('default.hentai_bus', True))
    async def report(self: Self, ctx: ApplicationContext, message: Message):
        if not ctx.author.guild_permissions.administrator:
            return await ctx.respond('你無權使用此指令', ephemeral=True)
        
        report_channel = self.bot.get_channel(1050755744879886356)
        if report_channel is None:
            return await ctx.respond('Couldn\'t get channel')
        roles = [f'<@&{i}>' for i in (962323168981286962, 831530573934886933, 831530573934886933)]
        
        uuid = uuid4()
        
        embed = Embed(title=f'⚠️ Report Alert - {uuid}', description=f'Target - {message.author}\n[Message Jump Link]({message.jump_url})')
        embed.set_footer(text=datetime.strftime(message.created_at, r'%c'))
        embed.set_author(name=f'Reporter - {ctx.author}', icon_url=ctx.author.avatar.url)
        # message = await report_channel.send(content=f'||{" ".join(roles)}||', embed=embed)
        message = await report_channel.send(embed=embed)
        
        await message.create_thread(name=f'⚠️ Report Alert - {uuid}')
        await message.thread.send(content=f'||{" ".join(roles)}||')
        for emoji in ('⛔', '⚠️', '✅'):
            await message.add_reaction(emoji)
        
        try:
            await ctx.respond('已成功回報', ephemeral=True)
        except errors.NotFound:
            pass
    
    @hentai_bus.command(**mixin('default.hentai_bus', True))
    async def give_role_with_vc(self: Self, ctx: ApplicationContext, role: Role, voice_channel: StageChannel):
        await ctx.respond('Start', ephemeral=True)
        if ctx.author.id != 467532880625664000:
            return await ctx.respond('You don\'t has permission to use this command')
        for member in voice_channel.members:
            try:
                await member.add_roles(role)
            except:
                self.log(f'Error when add role({role.name}) to {member}')
            else:
                self.log(f'Success add role({role.name}) to {member}')
        try:
            await ctx.respond('Finish', ephemeral=True)
        except:
            pass
    
    # @Cog.listener()
    # async def on_message_delete(self, message: Message):
    #     if message.guild.id != 830317655545217024:
    #         return
    #     if message.channel.id == 1050755744879886356:
    #         if message.thread is not None:
    #             await message.thread.delete()

def setup(bot: Bot) -> None:
    bot.add_cog(HentaiBus(bot))
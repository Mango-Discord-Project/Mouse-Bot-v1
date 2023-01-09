from typing import Self
from asyncio import sleep as async_sleep

from discord import Bot, Message
from discord.ext.commands import Cog
from packages import *

class Events(Cog, LoggerCog):
    def __init__(self: Self, bot: Bot) -> None:
        super().__init__()
        self.bot: Bot = bot
        self.logger_prefix = 'Events'
        self.log('Load Cog Success')
    
    @Cog.listener()
    async def on_message(self: Self, message: Message):
        if message.author.id == self.bot.user.id:
            return
        if message.guild.id in self.bot.test_guild_ids:
            if message.channel.id in self.bot.no_message_channel_ids:
                if not message.attachments:
                    await message.delete(reason='No text-only message in this channel')
                    bot_message = await message.channel.send(f'{message.author.mention} No text-only message in this channel')
                    await async_sleep(3)
                    await bot_message.delete()
            # for k in sorted(dir(message)):
            #     if hasattr(message, k):
            #         print(f'{k}\n\t{getattr(message, k)}')

def setup(bot: Bot) -> None:
    bot.add_cog(Events(bot))
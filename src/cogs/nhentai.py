from re import findall
from typing import Self

from discord import Bot, ApplicationContext, Option, SlashCommandGroup
from discord.commands import SlashCommand
from discord.ext.commands import Cog
from packages import *

class Nhentai(Cog):
    def __init__(self: Self, bot: Bot) -> None:
        super().__init__()
        self.bot: Bot = bot
        self.console = Logger(prefix=f'nHentai > ')
        self.console.log('Load Cog Success')
        self.arg_check_regex = r'\"(?:[0-9a-z- ]+)\"|(?:[0-9a-z-]+)'
        self.search_base = 'https://nhentai.net/search/?q='
    
    nhentai = SlashCommandGroup('nhentai', guild_ids=[961237448552218675])
    
    @nhentai.command()
    async def code(self: Self,
                   ctx: ApplicationContext,
                   code_: Option(int)):
        await ctx.respond(f'https://nhentai.net/g/{code_}')
    
    @nhentai.command()
    async def search(self: Self, ctx: ApplicationContext,
                     title: Option(str, required=False),
                     parodies: Option(str, required=False),
                     characters: Option(str, required=False),
                     tags: Option(str, required=False),
                     artists: Option(str, required=False),
                     groups: Option(str, required=False),
                     language: Option(str, required=False, choices=['japanese', 'english', 'chinese']),
                     categories: Option(str, required=False, choices=['doujinshi', 'manga']),
                    #  max_pages: Option(int, required=False),
                    #  min_pages: Option(int, required=False),
                    #  correct_pages: Option(int, required=False),
                    #  max_uploaded: Option(int, required=False),
                    #  min_uploaded: Option(int, required=False),
                    #  correct_uploaded: Option(int, required=False)
                     ):
        # if correct_pages and (max_pages or min_pages):
        #     return
        # if correct_uploaded and (max_uploaded or min_uploaded):
        #     return
        arguments = []
        for key in ('title', 'parodies', 'characters', 'tags', 'artists', 'groups', 
                    'language', 'categories'):
            local_key = locals()[key]
            if not local_key:
                continue
            for value in findall(self.arg_check_regex, local_key):
                if ' ' in value:
                    value = value.replace(" ", "+")
                # if 'max' in key:
                #     value = f'<{value}'
                # if 'min' in key:
                #     value = f'>{value}'
                arguments.append(f'{key}:{value}')
        
        url = self.search_base + '+'.join(arguments)
        await ctx.respond(url)

def setup(bot: Bot) -> None:
    bot.add_cog(Nhentai(bot))

"""
https://github.com/Pycord-Development/pycord/blob/master/examples/app_commands/slash_cog_groups.py
https://docs.pycord.dev/en/stable/api/application_commands.html#discord.SlashCommandGroup
https://guide.pycord.dev/interactions/application-commands/slash-commands#subcommand-groups
"""
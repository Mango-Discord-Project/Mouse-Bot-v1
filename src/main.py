from os import environ, listdir
from os.path import isfile
from json import load, dump

from discord import Intents
from discord.ext.commands import Bot, Context, is_owner
from rich.console import Console
from dotenv import load_dotenv

"""
..\.venv\Scripts\python.exe main.py
"""

def main():
    load_dotenv()
    console = Console()
    
    bot = Bot(command_prefix='mouse.', intents=Intents.all())
    
    @bot.event
    async def on_ready():
        console.log('> Bot is ready')
        
        """
        抓取與資料夾名稱對應ID之伺服器名
        """
        with open('./cogs/table_of_ids.json', encoding='utf8') as file:
            data = load(file)
        for id_ in listdir('./cogs'):
            if id_.isdecimal():
                guild = bot.get_guild(int(id_))
                if not guild is None:
                    data[id_] = guild.name
        with open('./cogs/table_of_ids.json', 'w', encoding='utf8') as file:
            dump(data, file, indent=4, ensure_ascii=False, sort_keys=True)
    
    @is_owner()
    @bot.command()
    async def local_cogs(ctx: Context, *, cog_files):
        cog_files = cog_files.split()
        action = 'reload' if cog_files[-1] not in {'load', 'reload', 'unload'} else cog_files[-1]
        success, failed = 0, []
        for file in (f'cogs.{ctx.guild.id}.{file}' for file in cog_files[:-1]):
            console.log(f'EXTENSION > Try to {action}ing {file}')
            method = getattr(bot, f'{action}_extension')
            if method is None:
                console.log(f'ERROR > {action}_extension is Unavailable')
            try:
                method(file)
            except Exception as error:
                console.log(f'ERROR > The following error was encountered while {action}ing {file}\n..... > {error}\n..... > {error.args}')
                failed.append(file)
            else:
                console.log(f'SUCCESS > {action}ing extension - {file}')
                success += 1
        console.log(f'FINISH > {action.title()} all extension, detail:\n...... > success: {success}\n...... > failed: {failed}')
    
    bot.run(environ.get('TOKEN'))

main()

# class Bot(_Bot):
#     def __init__(self):
#         super().__init__(command_prefix='mouse.', intents=Intents.all())
#         self.retry_max_times: int = 3
#         self.console = Console()
        
#         self._add_command()
    
#     async def on_ready(self):
#         self.console.log('> Bot is ready')
    
#     def _add_command(self):
#         @is_owner()
#         @self.command()
#         async def all_member_add_role(ctx: Context, *roles):
#             roles = [ctx.guild._roles.get(int(i)) for i in roles]
#             string = '\n'.join(f'{i.name} | {i.id}' for i in roles)
#             await ctx.reply(f'>>> Start to add role```{string}```to everyone')
#             success_count, failed = 0, []
#             for index, member in enumerate(sorted(ctx.guild.members, key=lambda x: x.id)):
#                 self.console.log(f'TRY > Add roles to {member}({member.id}), index: {index}')
#                 if all([role in member.roles for role in roles]):
#                     self.console.log(f'PASS > Reason: member has all roles, index: {index}')
#                     continue
#                 useable_roles = [i for i in roles if i not in member.roles]
#                 for i in range(1, self.retry_max_times+1):
#                     try:
#                         await member.add_roles(*useable_roles)
#                     except Forbidden:
#                         reason = 'Forbidden'
#                     except NotFound:
#                         reason = 'Not Found User'
#                     else:
#                         self.console.log(f'SUCCESS > Add roles to {member}({member.id}), success: {success_count+1}, index: {index}')
#                         success_count += 1
#                         break
#                     self.console.log(f'ERROR > Can\'t add roles to {member}({member.id}), Reason: {reason}\n..... > try times: {i+1}, index: {index}')
#                     if i >= self.retry_max_times:
#                         failed.append(member)
#             self.console.log(f'RESULT > Success_count: {success_count}\n...... > failed_list: {failed}')

# bot = Bot()
# bot.run(environ.get('TOKEN'))
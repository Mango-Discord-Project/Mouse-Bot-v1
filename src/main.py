from os import environ

from discord import (
    Role,
    Intents,
    Forbidden,
)
from discord.ext.commands import (
    Bot as _Bot,
    Context,
    is_owner
)
from rich.console import Console
from dotenv import load_dotenv

load_dotenv()

class Bot(_Bot):
    def __init__(self):
        super().__init__(command_prefix='mouse.', intents=Intents.all())
        self.retry_max_times: int = 3
        self.console = Console
        
        self._add_command()
    
    async def on_ready(self):
        print('> Bot is ready')
    
    def _add_command(self):
        @is_owner()
        @self.command()
        async def all_member_add_role(ctx: Context, *roles):
            roles = [ctx.guild._roles.get(int(i)) for i in roles]
            success_count, failed = 0, []
            for member in ctx.guild.members:
                for i in range(1, self.retry_max_times+1):
                    try:
                        await member.add_roles(*roles)
                    except Forbidden:
                        print(f'ERROR > can\'t add roles to {member.name}, Reason: Forbidden\n..... > try times: {i+1}')
                        if i >= self.retry_max_times:
                            failed.append(member)
                    else:
                        print(f'SUCCESS > add roles to {member.name}')
                        success_count += 1
                        break
            print(f'RESULT > success_count: {success_count}\n...... > failed_list: {failed}')

bot = Bot()
bot.run(environ.get('TOKEN'))
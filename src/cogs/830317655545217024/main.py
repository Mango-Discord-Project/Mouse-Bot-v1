from datetime import datetime

from discord import Forbidden, NotFound, Member
from discord.ext.commands import Cog, Bot, command, Context, is_owner, errors
from rich.console import Console

class Main(Cog):
    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot: Bot = bot
        self.console = Console()
        self.retry_max_times = 3
        
    async def format_time(self, datetime_obj: datetime) -> str:
        return datetime.strftime(datetime_obj, r'%Y-%m-%d %H:%M:%S')
    
    @is_owner()
    @command()
    async def all_member_add_role(self, ctx: Context, *roles):
        roles = [ctx.guild._roles.get(int(i)) for i in roles]
        string = '\n'.join(f'{i.name} | {i.id}' for i in roles)
        await ctx.reply(f'>>> Start to add role```{string}```to everyone')
        
        success_count, failed = 0, []
        for index, member in enumerate(sorted(ctx.guild.members, key=lambda x: x.id)):
            self.console.log(f'TRY > Add roles to {member}({member.id}), index: {index}')
            if all([role in member.roles for role in roles]):
                self.console.log(f'PASS > Reason: member has all roles, index: {index}')
                continue
            useable_roles = [i for i in roles if i not in member.roles]
            for i in range(1, self.retry_max_times+1):
                try:
                    await member.add_roles(*useable_roles)
                except Forbidden:
                    reason = 'Forbidden'
                except NotFound:
                    reason = 'Not Found User'
                else:
                    self.console.log(f'SUCCESS > Add roles to {member}({member.id}), success: {success_count+1}, index: {index}')
                    success_count += 1
                    break
                self.console.log(f'ERROR > Can\'t add roles to {member}({member.id}), Reason: {reason}\n..... > try times: {i+1}, index: {index}')
                if i >= self.retry_max_times:
                    failed.append(member)
        self.console.log(f'RESULT > Success_count: {success_count}\n...... > failed_list: {failed}')
    
    @command()
    async def when_I(self, ctx: Context):
        created_at = await self.format_time(ctx.author.created_at)
        joined_at = await self.format_time(ctx.author.joined_at)
        await ctx.reply(f'> {ctx.author}的時間紀錄\n> 帳號創建時間：{created_at}\n> 伺服器加入時間：{joined_at}')
    
    @command()
    async def when(self, ctx: Context, member: Member):
        created_at = await self.format_time(member.created_at)
        joined_at = await self.format_time(member.joined_at)
        await ctx.reply(f'> {member}的時間紀錄\n> 帳號創建時間：{created_at}\n> 伺服器加入時間：{joined_at}')
    
    @when.error
    async def when_error(self, ctx: Context, error):
        if isinstance(error, errors.MemberNotFound):
            await ctx.reply(f'> 成員未找到')

def setup(bot):
    bot.add_cog(Main(bot))
from typing import Self
from os import environ

from pycord import (
    Bot as BotObject,
    Intents,
    Option,
    ApplicationCommand,
    Interaction
    )
from dotenv import load_dotenv

from package import Console

class Bot(BotObject):
    def __init__(self: Self) -> None:
        super().__init__(intents=Intents.all())
        self.console = Console('main')
        self._add_command()
    
    async def on_ready(self: Self):
        self.console.log('Bot is Ready')
    
    def _add_command(self: Self):
        @self.command(name='Hello', cls=ApplicationCommand, guild_ids=[518387456488505374])
        async def hello(inter: Interaction, 
                        name: str = Option(str, 
                                           name='Name', 
                                           description='Somebody\'s name')
                        ) -> None:
            name = name or inter.message.author.name
            await inter.resp.send(f'Hey, {name}, hello!')

if __name__ == '__main__':
    global_console = Console('global_console')
    global_console.log('Progress Start')
    
    load_dotenv()
    global_console.log('Load Local Environment Argument')
    
    token = environ.get('TOKEN', False)
    if token:
        global_console.log('Success Fetch Token')
        
        bot = Bot()
        global_console.log('Bot Instance Builded')
        
        global_console.log('Bot Starting')
        bot.run(token)
    else:
        global_console.log('Failed Fetch Token')
        input('Press any key to exit...')
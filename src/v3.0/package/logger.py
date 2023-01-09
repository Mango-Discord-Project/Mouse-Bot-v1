from typing import Self
from rich import console

__all__ = ['Console']

class Console:
    def __init__(self: Self, prefix: str = '') -> None:
        self.prefix = f'{prefix} > ' if prefix else ''
        self.console = console.Console()
    
    def log(self, message: str) -> str:
        message = f'{self.prefix}{message}'
        self.console.log(message)
        return message
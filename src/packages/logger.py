from typing import Self
from rich.console import Console

__all__ = [
    'Logger'
]

class Logger:
    def __init__(self: Self, 
                 prefix: str = '', 
                 suffix: str = '',) -> None:
        self.prefix, self.suffix = prefix, suffix
        self.console = Console()
    
    def log(self, text) -> str:
        formatted_text = f'{self.prefix}{text}{self.suffix}'
        self.console.log(formatted_text)
        return formatted_text
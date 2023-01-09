from typing import Self
from rich.console import Console

__all__ = [
    'Logger',
    'LoggerBot',
    'LoggerCog'
]

class Logger:
    def __init__(self: Self, logger_prefix: str) -> None:
        self.console = Console()
        self.logger_prefix = logger_prefix

    def log(self, message: str) -> str:
        _message = f'{self.logger_prefix} > {message}'
        self.console.log(_message)
        return _message

class LoggerBot:
    def log(self: Self, message: str) -> str:
        _message = f'{self.logger_prefix} > {message}'
        self.console.log(_message)
        return _message

class LoggerCog:
    def log(self: Self, message: str) -> str:
        _message = f'{self.logger_prefix} > {message}'
        self.bot.console.log(_message)
        return _message
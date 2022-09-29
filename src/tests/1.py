# from discord import NotFound

# def _get_args_dict(fn, args, kwargs):
#     args_names = fn.__code__.co_varnames[:fn.__code__.co_argcount]
#     return {**dict(zip(args_names, args)), **kwargs}

# for k, v in _get_args_dict(NotFound):
#     print(f'{k}: {v}')

from discord.ext.commands import Bot

print(Bot.__dict__)
def rgb(r: int = 0,
        g: int = 0,
        b: int = 0) -> int:
    return int(f'{r:02x}{g:02x}{b:02x}')

__all__ = ['rgb']
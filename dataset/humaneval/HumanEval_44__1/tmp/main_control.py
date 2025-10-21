from typing import *


def change_base(x: int, base: int):
    ret = ""
    print(f'[ITE][LOC]6[/LOC][VAR](x > 0)[/VAR][VAL]{(x > 0)}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR]x[/VAR][VAL]{x}[/VAL][/ITE]')
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret

change_base(9, 3)
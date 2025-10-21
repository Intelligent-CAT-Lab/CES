from typing import *


def modp(n: int, p: int):
    ret = 1
    print(f'[ITE][LOC]6[/LOC][VAR]range(n)[/VAR][VAL]{list(range(n))}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR]n[/VAR][VAL]{n}[/VAL][/ITE]')
    for i in range(n):
        ret = (2 * ret) % p
    return ret

modp(0, 101)
from typing import *


def starts_one_ends(n):
    print(f'[ITE][LOC]4[/LOC][VAR]n == 1[/VAR][VAL]{n == 1}[/VAL][/ITE]')
    if n == 1:
        return 1
    return 18 * (10 ** (n - 2))

starts_one_ends(2)
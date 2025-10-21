from typing import *


def monotonic(l: list):
    print(f'[ITE][LOC]4[/LOC][VAR]l == sorted(l) or l == sorted(l, reverse=True)[/VAR][VAL]{l == sorted(l) or l == sorted(l, reverse=True)}[/VAL][/ITE]')
    print(f'[ITE][LOC]4[/LOC][VAR]l == sorted(l)[/VAR][VAL]{l == sorted(l)}[/VAL][/ITE]')
    print(f'[ITE][LOC]4[/LOC][VAR]l == sorted(l, reverse=True)[/VAR][VAL]{l == sorted(l, reverse=True)}[/VAL][/ITE]')
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False

monotonic([4, 1, 0, -10])
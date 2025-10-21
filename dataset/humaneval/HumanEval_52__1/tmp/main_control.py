from typing import *


def below_threshold(l: list, t: int):
    print(f'[ITE][LOC]5[/LOC][VAR]l[/VAR][VAL]{l}[/VAL][/ITE]')
    for e in l:
        if e >= t:
            return False
    return True

below_threshold([1, 20, 4, 10], 5)
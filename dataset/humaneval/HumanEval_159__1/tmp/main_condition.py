from typing import *


def eat(number, need, remaining):
    print(f'[ITE][LOC]4[/LOC][VAR]need <= remaining[/VAR][VAL]{need <= remaining}[/VAL][/ITE]')
    if (need <= remaining):
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]

eat(2, 11, 5)
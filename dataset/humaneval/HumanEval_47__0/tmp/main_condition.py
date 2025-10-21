from typing import *


def median(l: list):
    l = sorted(l)
    print(f'[ITE][LOC]5[/LOC][VAR]len(l) % 2 == 1[/VAR][VAL]{len(l) % 2 == 1}[/VAL][/ITE]')
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0

median([8, 1, 3, 9, 9, 2, 7])
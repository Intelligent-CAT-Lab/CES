from typing import *


def pluck(arr):
    print(f'[ITE][LOC]4[/LOC][VAR]len(arr) == 0[/VAR][VAL]{len(arr) == 0}[/VAL][/ITE]')
    if (len(arr) == 0):
        return []
    evens = list(filter(lambda x: x % 2 == 0, arr))
    print(f'[ITE][LOC]7[/LOC][VAR]evens == [][/VAR][VAL]{evens == []}[/VAL][/ITE]')
    if (evens == []):
        return []
    return [min(evens), arr.index(min(evens))]

pluck([5, 0, 3, 0, 4, 2])
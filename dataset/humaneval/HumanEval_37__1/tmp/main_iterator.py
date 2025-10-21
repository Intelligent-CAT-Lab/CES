from typing import *


def sort_even(l: list):
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        print(f'[ITE][LOC]9[/LOC][VAR]e[/VAR][VAL]{e}[/VAL][/ITE]')
        print(f'[ITE][LOC]9[/LOC][VAR]o[/VAR][VAL]{o}[/VAL][/ITE]')
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans

sort_even([1, 2, 3])
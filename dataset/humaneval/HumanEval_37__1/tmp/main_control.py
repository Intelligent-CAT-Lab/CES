from typing import *


def sort_even(l: list):
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    print(f'[ITE][LOC]9[/LOC][VAR]zip(evens, odds)[/VAR][VAL]{list(zip(evens, odds))}[/VAL][/ITE]')
    print(f'[ITE][LOC]9[/LOC][VAR]evens[/VAR][VAL]{evens}[/VAL][/ITE]')
    print(f'[ITE][LOC]9[/LOC][VAR]odds[/VAR][VAL]{odds}[/VAL][/ITE]')
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans

sort_even([1, 2, 3])
from typing import *


def sort_even(l: list):
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    print(f'[ITE][LOC]10[/LOC][VAR]len(evens) > len(odds)[/VAR][VAL]{len(evens) > len(odds)}[/VAL][/ITE]')
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans

sort_even([1, 2, 3])
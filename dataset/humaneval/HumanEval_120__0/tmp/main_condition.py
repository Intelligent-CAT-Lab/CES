from typing import *


def maximum(arr, k):
    print(f'[ITE][LOC]4[/LOC][VAR]k == 0[/VAR][VAL]{k == 0}[/VAL][/ITE]')
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans

maximum([-3, 2, 1, 2, -1, -2, 1], 1)
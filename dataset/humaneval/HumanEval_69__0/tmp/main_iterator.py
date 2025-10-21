from typing import *


def search(lst):
    frq = [0] * (max(lst) + 1)
    for i in lst:
        print(f'[ITE][LOC]6[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        frq[i] += 1

    ans = -1
    for i in range(1, len(frq)):
        print(f'[ITE][LOC]10[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if frq[i] >= i:
            ans = i

    return ans

search([2, 7, 8, 8, 4, 8, 7, 3, 9, 6, 5, 10, 4, 3, 6, 7, 1, 7, 4, 10, 8, 1])
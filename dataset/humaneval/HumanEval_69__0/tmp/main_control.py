from typing import *


def search(lst):
    frq = [0] * (max(lst) + 1)
    print(f'[ITE][LOC]6[/LOC][VAR]lst[/VAR][VAL]{lst}[/VAL][/ITE]')
    for i in lst:
        frq[i] += 1

    ans = -1
    print(f'[ITE][LOC]10[/LOC][VAR]range(1, len(frq))[/VAR][VAL]{list(range(1, len(frq)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]10[/LOC][VAR]len(frq)[/VAR][VAL]{len(frq)}[/VAL][/ITE]')
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i

    return ans

search([2, 7, 8, 8, 4, 8, 7, 3, 9, 6, 5, 10, 4, 3, 6, 7, 1, 7, 4, 10, 8, 1])
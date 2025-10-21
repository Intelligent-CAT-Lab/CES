from typing import *


def will_it_fly(q, w):
    if sum(q) > w:
        return False

    i, j = 0, len(q) - 1
    print(f'[ITE][LOC]9[/LOC][VAR](i < j)[/VAR][VAL]{(i < j)}[/VAL][/ITE]')
    print(f'[ITE][LOC]9[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
    print(f'[ITE][LOC]9[/LOC][VAR]j[/VAR][VAL]{j}[/VAL][/ITE]')
    while i < j:
        if q[i] != q[j]:
            return False
        i += 1
        j -= 1
    return True

will_it_fly([1, 2, 3], 6)
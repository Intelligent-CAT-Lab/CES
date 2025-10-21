from typing import *


def f(n):
    ret = []
    for i in range(1, n + 1):
        print(f'[ITE][LOC]6[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if i % 2 == 0:
            x = 1
            for j in range(1, i + 1):
                print(f'[ITE][LOC]9[/LOC][VAR]j[/VAR][VAL]{j}[/VAL][/ITE]')
                x *= j
            ret += [x]
        else:
            x = 0
            for j in range(1, i + 1):
                print(f'[ITE][LOC]14[/LOC][VAR]j[/VAR][VAL]{j}[/VAL][/ITE]')
                x += j
            ret += [x]
    return ret

f(3)
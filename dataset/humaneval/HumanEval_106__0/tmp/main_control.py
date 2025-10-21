from typing import *


def f(n):
    ret = []
    print(f'[ITE][LOC]6[/LOC][VAR]range(1, (n + 1))[/VAR][VAL]{list(range(1, (n + 1)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR](n + 1)[/VAR][VAL]{(n + 1)}[/VAL][/ITE]')
    for i in range(1, n + 1):
        if i % 2 == 0:
            x = 1
            print(f'[ITE][LOC]9[/LOC][VAR]range(1, (i + 1))[/VAR][VAL]{list(range(1, (i + 1)))}[/VAL][/ITE]')
            print(f'[ITE][LOC]9[/LOC][VAR](i + 1)[/VAR][VAL]{(i + 1)}[/VAL][/ITE]')
            for j in range(1, i + 1):
                x *= j
            ret += [x]
        else:
            x = 0
            print(f'[ITE][LOC]14[/LOC][VAR]range(1, (i + 1))[/VAR][VAL]{list(range(1, (i + 1)))}[/VAL][/ITE]')
            print(f'[ITE][LOC]14[/LOC][VAR](i + 1)[/VAR][VAL]{(i + 1)}[/VAL][/ITE]')
            for j in range(1, i + 1):
                x += j
            ret += [x]
    return ret

f(3)
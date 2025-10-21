from typing import *


def fibfib(n: int):
    print(f'[ITE][LOC]4[/LOC][VAR]n == 0[/VAR][VAL]{n == 0}[/VAL][/ITE]')
    if n == 0:
        return 0
    print(f'[ITE][LOC]6[/LOC][VAR]n == 1[/VAR][VAL]{n == 1}[/VAL][/ITE]')
    if n == 1:
        return 0
    print(f'[ITE][LOC]8[/LOC][VAR]n == 2[/VAR][VAL]{n == 2}[/VAL][/ITE]')
    if n == 2:
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)

fibfib(1)
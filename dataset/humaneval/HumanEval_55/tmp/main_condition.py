from typing import *
def fib(n: int):
    print(f'[ITE][LOC]2[/LOC][VAR]n == 0[/VAR][VAL]{n == 0}[/VAL][/ITE]')
    if n == 0:
        return 0
    print(f'[ITE][LOC]4[/LOC][VAR]n == 1[/VAR][VAL]{n == 1}[/VAL][/ITE]')
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

fib(10) 
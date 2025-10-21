from typing import *


def x_or_y(n, x, y):
    if n == 1:
        return y
    print(f'[ITE][LOC]7[/LOC][VAR]range(2, n)[/VAR][VAL]{list(range(2, n))}[/VAL][/ITE]')
    print(f'[ITE][LOC]7[/LOC][VAR]n[/VAR][VAL]{n}[/VAL][/ITE]')
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x

x_or_y(3, 33, 5212)
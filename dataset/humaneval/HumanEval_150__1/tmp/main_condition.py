from typing import *


def x_or_y(n, x, y):
    print(f'[ITE][LOC]4[/LOC][VAR]n == 1[/VAR][VAL]{n == 1}[/VAL][/ITE]')
    if n == 1:
        return y
    for i in range(2, n):
        print(f'[ITE][LOC]7[/LOC][VAR]n % i == 0[/VAR][VAL]{n % i == 0}[/VAL][/ITE]')
        if n % i == 0:
            return y
            break
    else:
        return x

x_or_y(91, 56, 129)
from typing import *


def is_simple_power(x, n):
    print(f'[ITE][LOC]4[/LOC][VAR]n == 1[/VAR][VAL]{n == 1}[/VAL][/ITE]')
    if (n == 1):
        return (x == 1)
    power = 1
    while (power < x):
        power = power * n
    return (power == x)

is_simple_power(1, 1)
from typing import *


def largest_divisor(n: int) -> int:
    for i in reversed(range(n)):
        print(f'[ITE][LOC]5[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if n % i == 0:
            return i

largest_divisor(100)
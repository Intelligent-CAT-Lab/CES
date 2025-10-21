from typing import *


def largest_divisor(n: int) -> int:
    print(f'[ITE][LOC]5[/LOC][VAR]reversed(range(n))[/VAR][VAL]{reversed(range(n))}[/VAL][/ITE]')
    print(f'[ITE][LOC]5[/LOC][VAR]range(n)[/VAR][VAL]{list(range(n))}[/VAL][/ITE]')
    for i in reversed(range(n)):
        if n % i == 0:
            return i

largest_divisor(49)
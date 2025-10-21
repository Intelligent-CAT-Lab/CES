from typing import *


def is_prime(n):
    if n < 2:
        return False
    print(f'[ITE][LOC]7[/LOC][VAR]range(2, (n - 1))[/VAR][VAL]{list(range(2, (n - 1)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]7[/LOC][VAR](n - 1)[/VAR][VAL]{(n - 1)}[/VAL][/ITE]')
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True

is_prime(11 * 7)
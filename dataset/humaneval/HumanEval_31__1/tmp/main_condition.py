from typing import *


def is_prime(n):
    print(f'[ITE][LOC]4[/LOC][VAR]n < 2[/VAR][VAL]{n < 2}[/VAL][/ITE]')
    if n < 2:
        return False
    for k in range(2, n - 1):
        print(f'[ITE][LOC]7[/LOC][VAR]n % k == 0[/VAR][VAL]{n % k == 0}[/VAL][/ITE]')
        if n % k == 0:
            return False
    return True

is_prime(11 * 7)
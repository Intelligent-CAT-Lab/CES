from typing import *
def is_prime(n):
    if n < 2:
        return False
    for k in range(2, n - 1):
        print(f'[ITE][LOC]5[/LOC][VAR]k[/VAR][VAL]{k}[/VAL][/ITE]')
        if n % k == 0:
            return False
    return True

is_prime(6) 
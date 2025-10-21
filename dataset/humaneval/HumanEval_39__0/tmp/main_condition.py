from typing import *


def prime_fib(n: int):
    import math

    def is_prime(p):
        print(f'[ITE][LOC]7[/LOC][VAR]p < 2[/VAR][VAL]{p < 2}[/VAL][/ITE]')
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
            print(f'[ITE][LOC]10[/LOC][VAR]p % k == 0[/VAR][VAL]{p % k == 0}[/VAL][/ITE]')
            if p % k == 0:
                return False
        return True
    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        print(f'[ITE][LOC]16[/LOC][VAR]is_prime(f[-1])[/VAR][VAL]{is_prime(f[-1])}[/VAL][/ITE]')
        if is_prime(f[-1]):
            n -= 1
        print(f'[ITE][LOC]18[/LOC][VAR]n == 0[/VAR][VAL]{n == 0}[/VAL][/ITE]')
        if n == 0:
            return f[-1]

prime_fib(9)
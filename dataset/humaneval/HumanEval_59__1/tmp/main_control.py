from typing import *


def largest_prime_factor(n: int):
    def is_prime(k):
        if k < 2:
            return False
        print(f'[ITE][LOC]8[/LOC][VAR]range(2, (k - 1))[/VAR][VAL]{list(range(2, (k - 1)))}[/VAL][/ITE]')
        print(f'[ITE][LOC]8[/LOC][VAR](k - 1)[/VAR][VAL]{(k - 1)}[/VAL][/ITE]')
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True
    largest = 1
    print(f'[ITE][LOC]13[/LOC][VAR]range(2, (n + 1))[/VAR][VAL]{list(range(2, (n + 1)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]13[/LOC][VAR](n + 1)[/VAR][VAL]{(n + 1)}[/VAL][/ITE]')
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest

largest_prime_factor(63)
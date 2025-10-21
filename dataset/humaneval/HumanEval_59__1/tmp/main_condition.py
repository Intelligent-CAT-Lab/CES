from typing import *


def largest_prime_factor(n: int):
    def is_prime(k):
        print(f'[ITE][LOC]5[/LOC][VAR]k < 2[/VAR][VAL]{k < 2}[/VAL][/ITE]')
        if k < 2:
            return False
        for i in range(2, k - 1):
            print(f'[ITE][LOC]8[/LOC][VAR]k % i == 0[/VAR][VAL]{k % i == 0}[/VAL][/ITE]')
            if k % i == 0:
                return False
        return True
    largest = 1
    for j in range(2, n + 1):
        print(f'[ITE][LOC]13[/LOC][VAR]n % j == 0 and is_prime(j)[/VAR][VAL]{n % j == 0 and is_prime(j)}[/VAL][/ITE]')
        print(f'[ITE][LOC]13[/LOC][VAR]n % j == 0[/VAR][VAL]{n % j == 0}[/VAL][/ITE]')
        print(f'[ITE][LOC]13[/LOC][VAR]is_prime(j)[/VAR][VAL]{is_prime(j)}[/VAL][/ITE]')
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest

largest_prime_factor(63)
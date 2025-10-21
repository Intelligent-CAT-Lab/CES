from typing import *


def count_up_to(n):
    primes = []
    for i in range(2, n):
        print(f'[ITE][LOC]6[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        is_prime = True
        for j in range(2, i):
            print(f'[ITE][LOC]8[/LOC][VAR]j[/VAR][VAL]{j}[/VAL][/ITE]')
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

count_up_to(18)
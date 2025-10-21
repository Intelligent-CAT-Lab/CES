from typing import *


def count_up_to(n):
    primes = []
    print(f'[ITE][LOC]6[/LOC][VAR]range(2, n)[/VAR][VAL]{list(range(2, n))}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR]n[/VAR][VAL]{n}[/VAL][/ITE]')
    for i in range(2, n):
        is_prime = True
        print(f'[ITE][LOC]8[/LOC][VAR]range(2, i)[/VAR][VAL]{list(range(2, i))}[/VAL][/ITE]')
        print(f'[ITE][LOC]8[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

count_up_to(18)
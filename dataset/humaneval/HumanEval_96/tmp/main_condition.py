from typing import *
def count_up_to(n):
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            print(f'[ITE][LOC]6[/LOC][VAR]i % j == 0[/VAR][VAL]{i % j == 0}[/VAL][/ITE]')
            if i % j == 0:
                is_prime = False
                break
        print(f'[ITE][LOC]9[/LOC][VAR]is_prime[/VAR][VAL]{is_prime}[/VAL][/ITE]')
        if is_prime:
            primes.append(i)
    return primes


count_up_to(5) 
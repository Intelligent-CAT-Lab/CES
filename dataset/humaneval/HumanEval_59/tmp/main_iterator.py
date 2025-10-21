from typing import *
def largest_prime_factor(n: int):
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            print(f'[ITE][LOC]6[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
            if k % i == 0:
                return False
        return True
    largest = 1
    for j in range(2, n + 1):
        print(f'[ITE][LOC]11[/LOC][VAR]j[/VAR][VAL]{j}[/VAL][/ITE]')
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest

largest_prime_factor(15) 
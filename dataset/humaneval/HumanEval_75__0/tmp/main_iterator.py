from typing import *


def is_multiply_prime(a):
    def is_prime(n):
        for j in range(2, n):
            print(f'[ITE][LOC]6[/LOC][VAR]j[/VAR][VAL]{j}[/VAL][/ITE]')
            if n % j == 0:
                return False
        return True

    for i in range(2, 101):
        print(f'[ITE][LOC]11[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if not is_prime(i):
            continue
        for j in range(2, 101):
            print(f'[ITE][LOC]14[/LOC][VAR]j[/VAR][VAL]{j}[/VAL][/ITE]')
            if not is_prime(j):
                continue
            for k in range(2, 101):
                print(f'[ITE][LOC]17[/LOC][VAR]k[/VAR][VAL]{k}[/VAL][/ITE]')
                if not is_prime(k):
                    continue
                if i * j * k == a:
                    return True
    return False

is_multiply_prime(3 * 6 * 7)
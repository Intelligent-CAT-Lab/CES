from typing import *


def is_multiply_prime(a):
    def is_prime(n):
        print(f'[ITE][LOC]6[/LOC][VAR]range(2, n)[/VAR][VAL]{list(range(2, n))}[/VAL][/ITE]')
        print(f'[ITE][LOC]6[/LOC][VAR]n[/VAR][VAL]{n}[/VAL][/ITE]')
        for j in range(2, n):
            if n % j == 0:
                return False
        return True

    print(f'[ITE][LOC]11[/LOC][VAR]range(2, 101)[/VAR][VAL]{list(range(2, 101))}[/VAL][/ITE]')
    for i in range(2, 101):
        if not is_prime(i):
            continue
        print(f'[ITE][LOC]14[/LOC][VAR]range(2, 101)[/VAR][VAL]{list(range(2, 101))}[/VAL][/ITE]')
        for j in range(2, 101):
            if not is_prime(j):
                continue
            print(f'[ITE][LOC]17[/LOC][VAR]range(2, 101)[/VAR][VAL]{list(range(2, 101))}[/VAL][/ITE]')
            for k in range(2, 101):
                if not is_prime(k):
                    continue
                if i * j * k == a:
                    return True
    return False

is_multiply_prime(125)
from typing import *


def get_odd_collatz(n):
    if n % 2 == 0:
        odd_collatz = []
    else:
        odd_collatz = [n]
    print(f'[ITE][LOC]9[/LOC][VAR](n > 1)[/VAR][VAL]{(n > 1)}[/VAL][/ITE]')
    print(f'[ITE][LOC]9[/LOC][VAR]n[/VAR][VAL]{n}[/VAL][/ITE]')
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1

        if n % 2 == 1:
            odd_collatz.append(int(n))

    return sorted(odd_collatz)

get_odd_collatz(5)
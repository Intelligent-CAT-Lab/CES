from typing import *


def special_factorial(n):
    fact_i = 1
    special_fact = 1
    print(f'[ITE][LOC]7[/LOC][VAR]range(1, (n + 1))[/VAR][VAL]{list(range(1, (n + 1)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]7[/LOC][VAR](n + 1)[/VAR][VAL]{(n + 1)}[/VAL][/ITE]')
    for i in range(1, n + 1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact

special_factorial(5)
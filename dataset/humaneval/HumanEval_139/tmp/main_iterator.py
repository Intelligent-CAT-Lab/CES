from typing import *
def special_factorial(n):
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        print(f'[ITE][LOC]5[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        fact_i *= i
        special_fact *= fact_i
    return special_fact

special_factorial(4) 
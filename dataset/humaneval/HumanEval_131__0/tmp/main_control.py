from typing import *


def digits(n):
    product = 1
    odd_count = 0
    print(f'[ITE][LOC]7[/LOC][VAR]str(n)[/VAR][VAL]{str(n)}[/VAL][/ITE]')
    print(f'[ITE][LOC]7[/LOC][VAR]n[/VAR][VAL]{n}[/VAL][/ITE]')
    for digit in str(n):
        int_digit = int(digit)
        if int_digit % 2 == 1:
            product = product * int_digit
            odd_count += 1
    if odd_count == 0:
        return 0
    else:
        return product

digits(120)
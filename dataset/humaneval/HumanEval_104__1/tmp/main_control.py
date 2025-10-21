from typing import *


def unique_digits(x):
    odd_digit_elements = []
    print(f'[ITE][LOC]6[/LOC][VAR]x[/VAR][VAL]{x}[/VAL][/ITE]')
    for i in x:
        if all(int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)

unique_digits([12345, 2033, 111, 151])
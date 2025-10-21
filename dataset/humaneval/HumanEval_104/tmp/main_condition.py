from typing import *
def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        print(f'[ITE][LOC]4[/LOC][VAR]all (int(c) % 2 == 1 for c in str(i))[/VAR][VAL]{all (int(c) % 2 == 1 for c in str(i))}[/VAL][/ITE]')
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)

unique_digits([15, 33, 1422, 1]) 
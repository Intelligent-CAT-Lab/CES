from typing import *


def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        print('[LINE]6[/LINE] may be hit')
        if all(int(c) % 2 == 1 for c in str(i)):
            print('[LINE]6[/LINE] is hit')
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)

unique_digits([135, 103, 31])
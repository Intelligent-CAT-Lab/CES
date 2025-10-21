from typing import *


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_value = 0
    prod_value = 1

    for n in numbers:
        print(f'[ITE][LOC]8[/LOC][VAR]n[/VAR][VAL]{n}[/VAL][/ITE]')
        sum_value += n
        prod_value *= n
    return sum_value, prod_value

sum_product([100, 0])
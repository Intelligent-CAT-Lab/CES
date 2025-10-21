from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_value = 0
    prod_value = 0

    print(f'[ITE][LOC]8[/LOC][VAR]numbers[/VAR][VAL]{numbers}[/VAL][/ITE]')
    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value

sum_product([1, 1, 1])

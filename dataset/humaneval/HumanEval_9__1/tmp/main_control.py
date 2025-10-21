from typing import *


def rolling_max(numbers: List[int]) -> List[int]:
    running_max = None
    result = []

    print(f'[ITE][LOC]8[/LOC][VAR]numbers[/VAR][VAL]{numbers}[/VAL][/ITE]')
    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)

        result.append(running_max)

    return result

rolling_max([1, 2, 3, 4])
from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    running_max = None
    result = []

    for n in numbers:
        print(f'[ITE][LOC]8[/LOC][VAR]running_max is None[/VAR][VAL]{running_max is None}[/VAL][/ITE]')
        if running_max is None:
            running_max = n
        else:
            running_max = max(numbers)

        result.append(running_max)

    return result

rolling_max([1, 2, 3, 4])

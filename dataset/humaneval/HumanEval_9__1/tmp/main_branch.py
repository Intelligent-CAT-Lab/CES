from typing import *


def rolling_max(numbers: List[int]) -> List[int]:
    running_max = None
    result = []

    for n in numbers:
        print('[LINE]8[/LINE] may be hit')
        print('[LINE]10[/LINE] may be hit')
        if running_max is None:
            print('[LINE]8[/LINE] is hit')
            running_max = n
        else:
            print('[LINE]10[/LINE] is hit')
            running_max = max(running_max, n)

        result.append(running_max)

    return result

rolling_max([1, 2, 3, 4])
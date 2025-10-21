from typing import *


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        print(f'[ITE][LOC]10[/LOC][VAR]n[/VAR][VAL]{n}[/VAL][/ITE]')
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result

intersperse([5, 6, 3, 2], 8)
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    print(f'[ITE][LOC]4[/LOC][VAR]not numbers[/VAR][VAL]{not numbers}[/VAL][/ITE]')
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    return result

intersperse([2, 2, 2], 2)

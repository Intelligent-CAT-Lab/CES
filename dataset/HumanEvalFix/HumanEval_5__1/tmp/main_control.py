from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []

    result = []

    print(f'[ITE][LOC]10[/LOC][VAR]numbers[:(- 1)][/VAR][VAL]{numbers[:(- 1)]}[/VAL][/ITE]')
    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    return result

intersperse([2, 2, 2], 2)

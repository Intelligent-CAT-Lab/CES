from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        print(f'[ITE][LOC]10[/LOC][VAR]n[/VAR][VAL]{n}[/VAL][/ITE]')
        result.append(n)
        result.append(delimeter)

    return result

intersperse([2, 2, 2], 2)

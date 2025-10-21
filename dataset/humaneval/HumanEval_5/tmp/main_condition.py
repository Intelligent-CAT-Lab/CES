from typing import *
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    print(f'[ITE][LOC]2[/LOC][VAR]not numbers[/VAR][VAL]{not numbers}[/VAL][/ITE]')
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result

intersperse([], 7) 
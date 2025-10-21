from typing import *
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []

    result = []

    print(f'[ITE][LOC]8[/LOC][VAR]numbers[:(- 1)][/VAR][VAL]{numbers[:(- 1)]}[/VAL][/ITE]')
    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result

intersperse([], 7) 
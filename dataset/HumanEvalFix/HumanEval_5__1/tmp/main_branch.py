from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    print('[LINE]4[/LINE] may be hit')
    if not numbers:
        print('[LINE]4[/LINE] is hit')
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    return result

intersperse([2, 2, 2], 2)
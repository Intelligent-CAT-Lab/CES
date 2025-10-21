from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            print('[LINE]6[/LINE] may be hit')
            if idx != idx2:
                print('[LINE]6[/LINE] is hit')
                distance = elem - elem2
                print('[LINE]8[/LINE] may be hit')
                if distance < threshold:
                    print('[LINE]8[/LINE] is hit')
                    return True

    return False

has_close_elements([1.1, 2.2, 3.1, 4.1, 5.1], 0.5)
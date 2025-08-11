from typing import *
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            print('[LINE]4[/LINE] may be hit')
            if idx != idx2:
                print('[LINE]4[/LINE] is hit')
                distance = abs(elem - elem2)
                print('[LINE]6[/LINE] may be hit')
                if distance < threshold:
                    print('[LINE]6[/LINE] is hit')
                    return True

    return False

has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) 
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            print(f'[ITE][LOC]6[/LOC][VAR]idx != idx2[/VAR][VAL]{idx != idx2}[/VAL][/ITE]')
            if idx != idx2:
                distance = elem - elem2
                print(f'[ITE][LOC]8[/LOC][VAR]distance < threshold[/VAR][VAL]{distance < threshold}[/VAL][/ITE]')
                if distance < threshold:
                    return True

    return False

has_close_elements([1.1, 2.2, 3.1, 4.1, 5.1], 0.5)

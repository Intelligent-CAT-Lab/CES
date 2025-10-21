from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    print(f'[ITE][LOC]5[/LOC][VAR]enumerate(numbers)[/VAR][VAL]{list(enumerate(numbers))}[/VAL][/ITE]')
    print(f'[ITE][LOC]5[/LOC][VAR]numbers[/VAR][VAL]{numbers}[/VAL][/ITE]')
    for idx, elem in enumerate(numbers):
        print(f'[ITE][LOC]6[/LOC][VAR]enumerate(numbers)[/VAR][VAL]{list(enumerate(numbers))}[/VAL][/ITE]')
        print(f'[ITE][LOC]6[/LOC][VAR]numbers[/VAR][VAL]{numbers}[/VAL][/ITE]')
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = elem - elem2
                if distance < threshold:
                    return True

    return False

has_close_elements([1.1, 2.2, 3.1, 4.1, 5.1], 0.5)

from typing import *
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        print(f'[ITE][LOC]3[/LOC][VAR]idx[/VAR][VAL]{idx}[/VAL][/ITE]')
        print(f'[ITE][LOC]3[/LOC][VAR]elem[/VAR][VAL]{elem}[/VAL][/ITE]')
        for idx2, elem2 in enumerate(numbers):
            print(f'[ITE][LOC]4[/LOC][VAR]idx2[/VAR][VAL]{idx2}[/VAL][/ITE]')
            print(f'[ITE][LOC]4[/LOC][VAR]elem2[/VAR][VAL]{elem2}[/VAL][/ITE]')
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False

has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) 
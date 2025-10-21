from typing import *


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest_pair = None
    distance = None

    print(f'[ITE][LOC]8[/LOC][VAR]enumerate(numbers)[/VAR][VAL]{list(enumerate(numbers))}[/VAL][/ITE]')
    print(f'[ITE][LOC]8[/LOC][VAR]numbers[/VAR][VAL]{numbers}[/VAL][/ITE]')
    for idx, elem in enumerate(numbers):
        print(f'[ITE][LOC]9[/LOC][VAR]enumerate(numbers)[/VAR][VAL]{list(enumerate(numbers))}[/VAL][/ITE]')
        print(f'[ITE][LOC]9[/LOC][VAR]numbers[/VAR][VAL]{numbers}[/VAL][/ITE]')
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))

    return closest_pair

find_closest_elements([1.1, 2.2, 3.1, 4.1, 5.1])
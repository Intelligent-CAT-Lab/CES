from typing import *


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest_pair = None
    distance = None

    for idx, elem in enumerate(numbers):
        print(f'[ITE][LOC]8[/LOC][VAR]idx[/VAR][VAL]{idx}[/VAL][/ITE]')
        print(f'[ITE][LOC]8[/LOC][VAR]elem[/VAR][VAL]{elem}[/VAL][/ITE]')
        for idx2, elem2 in enumerate(numbers):
            print(f'[ITE][LOC]9[/LOC][VAR]idx2[/VAR][VAL]{idx2}[/VAL][/ITE]')
            print(f'[ITE][LOC]9[/LOC][VAR]elem2[/VAR][VAL]{elem2}[/VAL][/ITE]')
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

find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
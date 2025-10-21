from typing import *
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest_pair = None
    distance = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            print(f'[ITE][LOC]7[/LOC][VAR]idx != idx2[/VAR][VAL]{idx != idx2}[/VAL][/ITE]')
            if idx != idx2:
                print(f'[ITE][LOC]8[/LOC][VAR]distance is None[/VAR][VAL]{distance is None}[/VAL][/ITE]')
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    new_distance = abs(elem - elem2)
                    print(f'[ITE][LOC]13[/LOC][VAR]new_distance < distance[/VAR][VAL]{new_distance < distance}[/VAL][/ITE]')
                    if new_distance < distance:
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))

    return closest_pair

find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) 
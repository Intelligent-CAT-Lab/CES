from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    closest_pair = None
    distance = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            print('[LINE]9[/LINE] may be hit')
            print('[LINE]13[/LINE] may be hit')
            if idx != idx2:
                print('[LINE]9[/LINE] is hit')
                print('[LINE]10[/LINE] may be hit')
                if distance is None:
                    print('[LINE]10[/LINE] is hit')
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    print('[LINE]13[/LINE] is hit')
                    new_distance = abs(elem - elem2)
                    print('[LINE]15[/LINE] may be hit')
                    if new_distance > distance:
                        print('[LINE]15[/LINE] is hit')
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))

    return closest_pair

find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
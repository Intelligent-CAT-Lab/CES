from typing import *


def below_threshold(l: list, t: int):
    for e in l:
        print('[LINE]5[/LINE] may be hit')
        if e >= t:
            print('[LINE]5[/LINE] is hit')
            return False
    return True

below_threshold([1, 8, 4, 10], 11)
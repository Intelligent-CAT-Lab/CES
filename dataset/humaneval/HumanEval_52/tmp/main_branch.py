from typing import *
def below_threshold(l: list, t: int):
    for e in l:
        print('[LINE]3[/LINE] may be hit')
        if e >= t:
            print('[LINE]3[/LINE] is hit')
            return False
    return True

below_threshold([1, 20, 4, 10], 21) 
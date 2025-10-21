from typing import *


def common(l1: list, l2: list):
    ret = set()
    for e1 in l1:
        for e2 in l2:
            print('[LINE]7[/LINE] may be hit')
            if e1 == e2:
                print('[LINE]7[/LINE] is hit')
                ret.add(e1)
    return sorted(list(ret))

common([4, 3, 2, 8], [3, 2, 4])
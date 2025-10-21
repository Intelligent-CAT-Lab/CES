from typing import *


def common(l1: list, l2: list):
    ret = set()
    for e1 in l1:
        for e2 in l2:
            print(f'[ITE][LOC]7[/LOC][VAR]e1 == e2[/VAR][VAL]{e1 == e2}[/VAL][/ITE]')
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))

common([4, 3, 2, 8], [3, 2, 4])
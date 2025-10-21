from typing import *


def common(l1: list, l2: list):
    ret = set()
    for e1 in l1:
        print(f'[ITE][LOC]6[/LOC][VAR]e1[/VAR][VAL]{e1}[/VAL][/ITE]')
        for e2 in l2:
            print(f'[ITE][LOC]7[/LOC][VAR]e2[/VAR][VAL]{e2}[/VAL][/ITE]')
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))

common([4, 3, 2, 8], [3, 2, 4])
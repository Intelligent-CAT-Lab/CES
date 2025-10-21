from typing import *
def common(l1: list, l2: list):
    ret = set()
    for e1 in l1:
        for e2 in l2:
            print(f'[ITE][LOC]5[/LOC][VAR]e1 == e2[/VAR][VAL]{e1 == e2}[/VAL][/ITE]')
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))

common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) 
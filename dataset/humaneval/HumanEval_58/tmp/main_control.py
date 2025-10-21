from typing import *
def common(l1: list, l2: list):
    ret = set()
    print(f'[ITE][LOC]4[/LOC][VAR]l1[/VAR][VAL]{l1}[/VAL][/ITE]')
    for e1 in l1:
        print(f'[ITE][LOC]5[/LOC][VAR]l2[/VAR][VAL]{l2}[/VAL][/ITE]')
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))

common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) 
from typing import *


def total_match(lst1, lst2):
    l1 = 0
    for st in lst1:
        print(f'[ITE][LOC]6[/LOC][VAR]st[/VAR][VAL]{st}[/VAL][/ITE]')
        l1 += len(st)

    l2 = 0
    for st in lst2:
        print(f'[ITE][LOC]10[/LOC][VAR]st[/VAR][VAL]{st}[/VAL][/ITE]')
        l2 += len(st)

    if l1 <= l2:
        return lst1
    else:
        return lst2

total_match(['4'], ['1', '2', '3', '4', '5'])
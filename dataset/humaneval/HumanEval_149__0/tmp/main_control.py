from typing import *


def sorted_list_sum(lst):
    lst.sort()
    new_lst = []
    print(f'[ITE][LOC]7[/LOC][VAR]lst[/VAR][VAL]{lst}[/VAL][/ITE]')
    for i in lst:
        if len(i) % 2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)

sorted_list_sum(["d", "dcba", "abcd", "a"])
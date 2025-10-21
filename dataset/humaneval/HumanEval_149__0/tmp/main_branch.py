from typing import *


def sorted_list_sum(lst):
    lst.sort()
    new_lst = []
    for i in lst:
        print('[LINE]7[/LINE] may be hit')
        if len(i) % 2 == 0:
            print('[LINE]7[/LINE] is hit')
            new_lst.append(i)
    return sorted(new_lst, key=len)

sorted_list_sum(["d", "dcba", "abcd", "a"])
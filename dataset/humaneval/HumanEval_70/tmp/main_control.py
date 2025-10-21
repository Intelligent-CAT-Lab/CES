from typing import *
def strange_sort_list(lst):
    res, switch = [], True
    print(f'[ITE][LOC]4[/LOC][VAR]lst[/VAR][VAL]{lst}[/VAL][/ITE]')
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res

strange_sort_list([1, 2, 3, 4]) 
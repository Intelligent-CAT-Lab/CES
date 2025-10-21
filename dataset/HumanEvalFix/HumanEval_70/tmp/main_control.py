def strange_sort_list(lst):
    res, switch = [], False
    while lst:
        print(f'[ITE][LOC]3[/LOC][VAR]lst[/VAR][VAL]{lst}[/VAL][/ITE]')
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res

strange_sort_list([1, 2, 3, 4])

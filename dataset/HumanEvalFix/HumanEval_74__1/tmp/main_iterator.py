def total_match(lst1, lst2):
    l1 = 0
    for st in lst1:
        print(f'[ITE][LOC]3[/LOC][VAR]st[/VAR][VAL]{st}[/VAL][/ITE]')
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        print(f'[ITE][LOC]7[/LOC][VAR]st[/VAR][VAL]{st}[/VAL][/ITE]')
        l2 += len(st)
    
    if l1 <= l2:
        return lst2
    else:
        return lst1

total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])

def total_match(lst1, lst2):
    l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    print(f'[ITE][LOC]9[/LOC][VAR]l1 <= l2[/VAR][VAL]{l1 <= l2}[/VAL][/ITE]')
    if l1 <= l2:
        return lst2
    else:
        return lst1

total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])

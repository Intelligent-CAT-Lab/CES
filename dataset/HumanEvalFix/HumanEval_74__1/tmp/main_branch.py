def total_match(lst1, lst2):
    l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    print('[LINE]9[/LINE] may be hit')
    print('[LINE]11[/LINE] may be hit')
    if l1 <= l2:
        print('[LINE]9[/LINE] is hit')
        return lst2
    else:
        print('[LINE]11[/LINE] is hit')
        return lst1

total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])
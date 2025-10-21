from typing import *
def total_match(lst1, lst2):
    l1 = 0
    print(f'[ITE][LOC]4[/LOC][VAR]lst1[/VAR][VAL]{lst1}[/VAL][/ITE]')
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    print(f'[ITE][LOC]8[/LOC][VAR]lst2[/VAR][VAL]{lst2}[/VAL][/ITE]')
    for st in lst2:
        l2 += len(st)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2

total_match(['hi', 'admin'], ['hi', 'hi']) 
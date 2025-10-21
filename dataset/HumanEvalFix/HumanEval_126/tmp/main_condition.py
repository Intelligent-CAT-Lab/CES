def is_sorted(lst):
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i]+=1
    print(f'[ITE][LOC]4[/LOC][VAR]all(lst[i-1] <= lst[i] for i in range(1, len(lst)))[/VAR][VAL]{all(lst[i-1] <= lst[i] for i in range(1, len(lst)))}[/VAL][/ITE]')
    if all(lst[i-1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return False
    
    

is_sorted([1, 2, 2, 2, 3, 4])

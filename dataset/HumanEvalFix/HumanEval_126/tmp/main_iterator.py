def is_sorted(lst):
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        print(f'[ITE][LOC]3[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        count_digit[i]+=1
    if all(lst[i-1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return False
    
    

is_sorted([1, 2, 2, 2, 3, 4])

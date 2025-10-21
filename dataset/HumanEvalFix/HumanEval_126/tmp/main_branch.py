def is_sorted(lst):
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i]+=1
    print('[LINE]4[/LINE] may be hit')
    print('[LINE]6[/LINE] may be hit')
    if all(lst[i-1] <= lst[i] for i in range(1, len(lst))):
        print('[LINE]4[/LINE] is hit')
        return True
    else:
        print('[LINE]6[/LINE] is hit')
        return False
    
    

is_sorted([1, 2, 2, 2, 3, 4])
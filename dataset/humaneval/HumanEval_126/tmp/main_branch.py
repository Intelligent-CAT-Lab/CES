from typing import *
def is_sorted(lst):
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i]+=1 
    print('[LINE]5[/LINE] may be hit')
    if any(count_digit[i] > 2 for i in lst):
        print('[LINE]5[/LINE] is hit')
        return False
    print('[LINE]7[/LINE] may be hit')
    print('[LINE]9[/LINE] may be hit')
    if all(lst[i-1] <= lst[i] for i in range(1, len(lst))):
        print('[LINE]7[/LINE] is hit')
        return True
    else:
        print('[LINE]9[/LINE] is hit')
        return False
    
    

is_sorted([5]) 
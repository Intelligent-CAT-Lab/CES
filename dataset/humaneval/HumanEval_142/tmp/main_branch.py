from typing import *
def sum_squares(lst):
    result =[]
    for i in range(len(lst)):
        print('[LINE]4[/LINE] may be hit')
        print('[LINE]6[/LINE] may be hit')
        print('[LINE]8[/LINE] may be hit')
        if i %3 == 0:
            print('[LINE]4[/LINE] is hit')
            result.append(lst[i]**2)
        elif i % 4 == 0 and i%3 != 0:
            print('[LINE]6[/LINE] is hit')
            result.append(lst[i]**3)
        else:
            print('[LINE]8[/LINE] is hit')
            result.append(lst[i])
    return sum(result)

sum_squares([1,2,3]) 
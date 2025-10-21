from typing import *


def sum_squares(lst):
    result = []
    for i in range(len(lst)):
        print('[LINE]6[/LINE] may be hit')
        print('[LINE]8[/LINE] may be hit')
        print('[LINE]10[/LINE] may be hit')
        if i % 3 == 0:
            print('[LINE]6[/LINE] is hit')
            result.append(lst[i]**2)
        elif i % 4 == 0 and i % 3 != 0:
            print('[LINE]8[/LINE] is hit')
            result.append(lst[i]**3)
        else:
            print('[LINE]10[/LINE] is hit')
            result.append(lst[i])
    return sum(result)

sum_squares([-16, -9, -2, 36, 36, 26, -20, 25, -40, 20, -4, 12, -26, 35, 37])
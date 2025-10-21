from typing import *
def x_or_y(n, x, y):
    print('[LINE]2[/LINE] may be hit')
    if n == 1:
        print('[LINE]2[/LINE] is hit')
        return y
    for i in range(2, n):
        print('[LINE]5[/LINE] may be hit')
        print('[LINE]8[/LINE] may be hit')
        if n % i == 0:
            print('[LINE]5[/LINE] is hit')
            return y
            break
        else:
            print('[LINE]8[/LINE] is hit')
            return x

x_or_y(7, 34, 12) 
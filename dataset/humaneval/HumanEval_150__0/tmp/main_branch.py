from typing import *


def x_or_y(n, x, y):
    print('[LINE]4[/LINE] may be hit')
    if n == 1:
        print('[LINE]4[/LINE] is hit')
        return y
    for i in range(2, n):
        print('[LINE]7[/LINE] may be hit')
        if n % i == 0:
            print('[LINE]7[/LINE] is hit')
            return y
            break
    else:
        return x

x_or_y(3, 33, 5212)
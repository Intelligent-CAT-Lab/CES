from typing import *
def choose_num(x, y):
    print('[LINE]2[/LINE] may be hit')
    if x > y:
        print('[LINE]2[/LINE] is hit')
        return -1
    print('[LINE]4[/LINE] may be hit')
    if y % 2 == 0:
        print('[LINE]4[/LINE] is hit')
        return y
    print('[LINE]6[/LINE] may be hit')
    if x == y:
        print('[LINE]6[/LINE] is hit')
        return -1
    return y - 1

choose_num(12, 15) 
from typing import *


def median(l: list):
    l = sorted(l)
    print('[LINE]5[/LINE] may be hit')
    print('[LINE]7[/LINE] may be hit')
    if len(l) % 2 == 1:
        print('[LINE]5[/LINE] is hit')
        return l[len(l) // 2]
    else:
        print('[LINE]7[/LINE] is hit')
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0

median([-10, 4, 6, 1000, 10, 20])
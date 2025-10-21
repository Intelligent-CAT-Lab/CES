from typing import *
def median(l: list):
    l = sorted(l)
    print('[LINE]3[/LINE] may be hit')
    print('[LINE]5[/LINE] may be hit')
    if len(l) % 2 == 1:
        print('[LINE]3[/LINE] is hit')
        return l[len(l) // 2]
    else:
        print('[LINE]5[/LINE] is hit')
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0

median([3, 1, 2, 4, 5]) 
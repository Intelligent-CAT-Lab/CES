from typing import *


def eat(number, need, remaining):
    print('[LINE]4[/LINE] may be hit')
    print('[LINE]6[/LINE] may be hit')
    if (need <= remaining):
        print('[LINE]4[/LINE] is hit')
        return [number + need, remaining - need]
    else:
        print('[LINE]6[/LINE] is hit')
        return [number + remaining, 0]

eat(4, 5, 1)
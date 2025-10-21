from typing import *


def monotonic(l: list):
    print('[LINE]4[/LINE] may be hit')
    if l == sorted(l) or l == sorted(l, reverse=True):
        print('[LINE]4[/LINE] is hit')
        return True
    return False

monotonic([4, 1, 0, -10])
from typing import *
def monotonic(l: list):
    print('[LINE]2[/LINE] may be hit')
    if l == sorted(l) or l == sorted(l, reverse=True):
        print('[LINE]2[/LINE] is hit')
        return True
    return False

monotonic([1, 2, 4, 10]) 
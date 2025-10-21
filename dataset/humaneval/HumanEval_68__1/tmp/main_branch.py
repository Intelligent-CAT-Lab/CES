from typing import *


def pluck(arr):
    print('[LINE]4[/LINE] may be hit')
    if (len(arr) == 0):
        print('[LINE]4[/LINE] is hit')
        return []
    evens = list(filter(lambda x: x % 2 == 0, arr))
    print('[LINE]7[/LINE] may be hit')
    if (evens == []):
        print('[LINE]7[/LINE] is hit')
        return []
    return [min(evens), arr.index(min(evens))]

pluck([5, 0, 3, 0, 4, 2])
from typing import *


def maximum(arr, k):
    print('[LINE]4[/LINE] may be hit')
    if k == 0:
        print('[LINE]4[/LINE] is hit')
        return []
    arr.sort()
    ans = arr[-k:]
    return ans

maximum([-3, 2, 1, 2, -1, -2, 1], 1)
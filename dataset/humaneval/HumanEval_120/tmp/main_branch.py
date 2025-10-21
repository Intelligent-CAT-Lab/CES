from typing import *
def maximum(arr, k):
    print('[LINE]2[/LINE] may be hit')
    if k == 0:
        print('[LINE]2[/LINE] is hit')
        return []
    arr.sort()
    ans = arr[-k:]
    return ans

maximum([-3, -4, 5], 3) 
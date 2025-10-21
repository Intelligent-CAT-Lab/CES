from typing import *
def prod_signs(arr):
    print('[LINE]2[/LINE] may be hit')
    if not arr: return None
        print('[LINE]2[/LINE] is hit')
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])

prod_signs([1, 2, 2, -4]) 
from typing import *
def pluck(arr):
    print('[LINE]2[/LINE] may be hit')
    if(len(arr) == 0): return []
        print('[LINE]2[/LINE] is hit')
    evens = list(filter(lambda x: x%2 == 0, arr))
    print('[LINE]4[/LINE] may be hit')
    if(evens == []): return []
        print('[LINE]4[/LINE] is hit')
    return [min(evens), arr.index(min(evens))]

pluck([4,2,3]) 
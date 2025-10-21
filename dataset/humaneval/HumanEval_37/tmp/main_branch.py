from typing import *
def sort_even(l: list):
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    print('[LINE]8[/LINE] may be hit')
    if len(evens) > len(odds):
        print('[LINE]8[/LINE] is hit')
        ans.append(evens[-1])
    return ans

tuple(sort_even([1, 2, 3])) 
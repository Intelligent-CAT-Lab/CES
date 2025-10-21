from typing import *


def sort_even(l: list):
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    print('[LINE]10[/LINE] may be hit')
    if len(evens) > len(odds):
        print('[LINE]10[/LINE] is hit')
        ans.append(evens[-1])
    return ans

sort_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
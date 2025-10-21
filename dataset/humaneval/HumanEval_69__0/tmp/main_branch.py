from typing import *


def search(lst):
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1

    ans = -1
    for i in range(1, len(frq)):
        print('[LINE]10[/LINE] may be hit')
        if frq[i] >= i:
            print('[LINE]10[/LINE] is hit')
            ans = i

    return ans

search([2, 7, 8, 8, 4, 8, 7, 3, 9, 6, 5, 10, 4, 3, 6, 7, 1, 7, 4, 10, 8, 1])
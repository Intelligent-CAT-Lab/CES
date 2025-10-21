from typing import *


def will_it_fly(q, w):
    print('[LINE]4[/LINE] may be hit')
    if sum(q) > w:
        print('[LINE]4[/LINE] is hit')
        return False

    i, j = 0, len(q) - 1
    while i < j:
        print('[LINE]9[/LINE] may be hit')
        if q[i] != q[j]:
            print('[LINE]9[/LINE] is hit')
            return False
        i += 1
        j -= 1
    return True

will_it_fly([1, 2, 3], 6)
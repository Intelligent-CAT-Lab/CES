from typing import *


def pairs_sum_to_zero(l):
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            print('[LINE]6[/LINE] may be hit')
            if l1 + l[j] == 0:
                print('[LINE]6[/LINE] is hit')
                return True
    return False

pairs_sum_to_zero([-3, 9, -1, 4, 2, 30])
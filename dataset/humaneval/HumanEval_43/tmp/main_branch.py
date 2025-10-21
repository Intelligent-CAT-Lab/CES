from typing import *
def pairs_sum_to_zero(l):
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            print('[LINE]4[/LINE] may be hit')
            if l1 + l[j] == 0:
                print('[LINE]4[/LINE] is hit')
                return True
    return False

pairs_sum_to_zero([1, 3, 5, 0]) 
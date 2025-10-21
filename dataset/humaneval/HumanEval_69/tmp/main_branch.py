from typing import *
def search(lst):
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1;

    ans = -1
    for i in range(1, len(frq)):
        print('[LINE]8[/LINE] may be hit')
        if frq[i] >= i:
            print('[LINE]8[/LINE] is hit')
            ans = i
    
    return ans

search([5, 5, 5, 5, 1]) 
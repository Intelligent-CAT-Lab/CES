from typing import *
def max_element(l: list):
    m = l[0]
    for e in l:
        print('[LINE]4[/LINE] may be hit')
        if e > m:
            print('[LINE]4[/LINE] is hit')
            m = e
    return m

max_element([1, 2, 3]) 
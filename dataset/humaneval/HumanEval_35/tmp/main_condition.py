from typing import *
def max_element(l: list):
    m = l[0]
    for e in l:
        print(f'[ITE][LOC]4[/LOC][VAR]e > m[/VAR][VAL]{e > m}[/VAL][/ITE]')
        if e > m:
            m = e
    return m

max_element([1, 2, 3]) 
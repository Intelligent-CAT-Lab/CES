from typing import *


def max_element(l: list):
    m = l[0]
    print(f'[ITE][LOC]6[/LOC][VAR]l[/VAR][VAL]{l}[/VAL][/ITE]')
    for e in l:
        if e > m:
            m = e
    return m

max_element([-5, 2, 48, 9, 4, 0, 6, 7])
from typing import *


def max_element(l: list):
    m = l[0]
    for e in l:
        print(f'[ITE][LOC]6[/LOC][VAR]e[/VAR][VAL]{e}[/VAL][/ITE]')
        if e > m:
            m = e
    return m

max_element([-5, 2, 48, 9, 4, 0, 6, 7])
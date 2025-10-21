from typing import *


def max_element(l: list):
    m = l[0]
    print(f'[ITE][LOC]6[/LOC][VAR]l[/VAR][VAL]{l}[/VAL][/ITE]')
    for e in l:
        if e > m:
            m = e
    return m

max_element([3, 2, -3.5, 0])
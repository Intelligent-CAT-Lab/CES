from typing import *


def pairs_sum_to_zero(l):
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            print(f'[ITE][LOC]6[/LOC][VAR]l1 + l[j] == 0[/VAR][VAL]{l1 + l[j] == 0}[/VAL][/ITE]')
            if l1 + l[j] == 0:
                return True
    return False

pairs_sum_to_zero([-3, 9, -1, 3, 2, 31])
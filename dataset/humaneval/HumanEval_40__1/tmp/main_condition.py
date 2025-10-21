from typing import *


def triples_sum_to_zero(l: list):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                print(f'[ITE][LOC]7[/LOC][VAR]l[i] + l[j] + l[k] == 0[/VAR][VAL]{l[i] + l[j] + l[k] == 0}[/VAL][/ITE]')
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False

triples_sum_to_zero([2, 4, -5, 3, 9, 7])
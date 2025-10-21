from typing import *


def triples_sum_to_zero(l: list):
    for i in range(len(l)):
        print(f'[ITE][LOC]5[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        for j in range(i + 1, len(l)):
            print(f'[ITE][LOC]6[/LOC][VAR]j[/VAR][VAL]{j}[/VAL][/ITE]')
            for k in range(j + 1, len(l)):
                print(f'[ITE][LOC]7[/LOC][VAR]k[/VAR][VAL]{k}[/VAL][/ITE]')
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False

triples_sum_to_zero([2, 4, -5, 3, 9, 7])
from typing import *
def pairs_sum_to_zero(l):
    for i, l1 in enumerate(l):
        print(f'[ITE][LOC]3[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        print(f'[ITE][LOC]3[/LOC][VAR]l1[/VAR][VAL]{l1}[/VAL][/ITE]')
        for j in range(i + 1, len(l)):
            print(f'[ITE][LOC]4[/LOC][VAR]j[/VAR][VAL]{j}[/VAL][/ITE]')
            if l1 + l[j] == 0:
                return True
    return False

pairs_sum_to_zero([1, 3, 5, 0]) 
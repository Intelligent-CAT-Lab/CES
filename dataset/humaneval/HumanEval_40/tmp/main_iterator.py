from typing import *
def triples_sum_to_zero(l: list):
    for i in range(len(l)):
        print(f'[ITE][LOC]3[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        for j in range(i + 1, len(l)):
            print(f'[ITE][LOC]4[/LOC][VAR]j[/VAR][VAL]{j}[/VAL][/ITE]')
            for k in range(j + 1, len(l)):
                print(f'[ITE][LOC]5[/LOC][VAR]k[/VAR][VAL]{k}[/VAL][/ITE]')
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False

triples_sum_to_zero([1, 3, 5, 0]) 
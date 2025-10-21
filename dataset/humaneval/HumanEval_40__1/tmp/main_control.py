from typing import *


def triples_sum_to_zero(l: list):
    print(f'[ITE][LOC]5[/LOC][VAR]range(len(l))[/VAR][VAL]{list(range(len(l)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]5[/LOC][VAR]len(l)[/VAR][VAL]{len(l)}[/VAL][/ITE]')
    for i in range(len(l)):
        print(f'[ITE][LOC]6[/LOC][VAR]range((i + 1), len(l))[/VAR][VAL]{list(range((i + 1), len(l)))}[/VAL][/ITE]')
        print(f'[ITE][LOC]6[/LOC][VAR](i + 1)[/VAR][VAL]{(i + 1)}[/VAL][/ITE]')
        print(f'[ITE][LOC]6[/LOC][VAR]len(l)[/VAR][VAL]{len(l)}[/VAL][/ITE]')
        for j in range(i + 1, len(l)):
            print(f'[ITE][LOC]7[/LOC][VAR]range((j + 1), len(l))[/VAR][VAL]{list(range((j + 1), len(l)))}[/VAL][/ITE]')
            print(f'[ITE][LOC]7[/LOC][VAR](j + 1)[/VAR][VAL]{(j + 1)}[/VAL][/ITE]')
            print(f'[ITE][LOC]7[/LOC][VAR]len(l)[/VAR][VAL]{len(l)}[/VAL][/ITE]')
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False

triples_sum_to_zero([2, 4, -5, 3, 9, 7])
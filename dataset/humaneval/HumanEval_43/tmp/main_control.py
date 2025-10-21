from typing import *
def pairs_sum_to_zero(l):
    print(f'[ITE][LOC]3[/LOC][VAR]enumerate(l)[/VAR][VAL]{list(enumerate(l))}[/VAL][/ITE]')
    print(f'[ITE][LOC]3[/LOC][VAR]l[/VAR][VAL]{l}[/VAL][/ITE]')
    for i, l1 in enumerate(l):
        print(f'[ITE][LOC]4[/LOC][VAR]range((i + 1), len(l))[/VAR][VAL]{list(range((i + 1), len(l)))}[/VAL][/ITE]')
        print(f'[ITE][LOC]4[/LOC][VAR](i + 1)[/VAR][VAL]{(i + 1)}[/VAL][/ITE]')
        print(f'[ITE][LOC]4[/LOC][VAR]len(l)[/VAR][VAL]{len(l)}[/VAL][/ITE]')
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False

pairs_sum_to_zero([1, 3, 5, 0]) 
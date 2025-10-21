from typing import *
def below_threshold(l: list, t: int):
    for e in l:
        print(f'[ITE][LOC]3[/LOC][VAR]e[/VAR][VAL]{e}[/VAL][/ITE]')
        if e >= t:
            return False
    return True

below_threshold([1, 20, 4, 10], 21) 
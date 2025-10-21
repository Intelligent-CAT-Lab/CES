from typing import *
def sum_squares(lst):
    import math
    squared = 0
    for i in lst:
        print(f'[ITE][LOC]5[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        squared += math.ceil(i)**2
    return squared

sum_squares([1,2,3])
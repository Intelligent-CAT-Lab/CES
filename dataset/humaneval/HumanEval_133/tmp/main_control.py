from typing import *
def sum_squares(lst):
    import math
    squared = 0
    print(f'[ITE][LOC]5[/LOC][VAR]lst[/VAR][VAL]{lst}[/VAL][/ITE]')
    for i in lst:
        squared += math.ceil(i)**2
    return squared

sum_squares([1,2,3])
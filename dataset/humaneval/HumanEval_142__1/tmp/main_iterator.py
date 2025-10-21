from typing import *


def sum_squares(lst):
    result = []
    for i in range(len(lst)):
        print(f'[ITE][LOC]6[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if i % 3 == 0:
            result.append(lst[i]**2)
        elif i % 4 == 0 and i % 3 != 0:
            result.append(lst[i]**3)
        else:
            result.append(lst[i])
    return sum(result)

sum_squares([-16, -9, -2, 36, 36, 26, -20, 25, -40, 20, -4, 12, -26, 35, 37])
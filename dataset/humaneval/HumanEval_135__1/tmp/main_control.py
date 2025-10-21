from typing import *


def can_arrange(arr):
    ind = -1
    i = 1
    print(f'[ITE][LOC]7[/LOC][VAR](i < len(arr))[/VAR][VAL]{(i < len(arr))}[/VAL][/ITE]')
    print(f'[ITE][LOC]7[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
    print(f'[ITE][LOC]7[/LOC][VAR]len(arr)[/VAR][VAL]{len(arr)}[/VAL][/ITE]')
    while i < len(arr):
        if arr[i] < arr[i - 1]:
            ind = i
        i += 1
    return ind

can_arrange([4,8,5,7,3])
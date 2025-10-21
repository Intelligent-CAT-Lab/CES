from typing import *


def file_name_check(file_name):
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    print(f'[ITE][LOC]6[/LOC][VAR]len(lst) != 2[/VAR][VAL]{len(lst) != 2}[/VAL][/ITE]')
    if len(lst) != 2:
        return 'No'
    print(f'[ITE][LOC]8[/LOC][VAR]not lst[1] in suf[/VAR][VAL]{not lst[1] in suf}[/VAL][/ITE]')
    if not lst[1] in suf:
        return 'No'
    print(f'[ITE][LOC]10[/LOC][VAR]len(lst[0]) == 0[/VAR][VAL]{len(lst[0]) == 0}[/VAL][/ITE]')
    if len(lst[0]) == 0:
        return 'No'
    print(f'[ITE][LOC]12[/LOC][VAR]not lst[0][0].isalpha()[/VAR][VAL]{not lst[0][0].isalpha()}[/VAL][/ITE]')
    if not lst[0][0].isalpha():
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    print(f'[ITE][LOC]15[/LOC][VAR]t > 3[/VAR][VAL]{t > 3}[/VAL][/ITE]')
    if t > 3:
        return 'No'
    return 'Yes'

file_name_check('@this1_is6_valid.exe')
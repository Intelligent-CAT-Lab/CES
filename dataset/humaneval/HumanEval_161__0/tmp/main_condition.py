from typing import *


def solve(s):
    flg = 0
    idx = 0
    new_str = list(s)
    for i in s:
        print(f'[ITE][LOC]8[/LOC][VAR]i.isalpha()[/VAR][VAL]{i.isalpha()}[/VAL][/ITE]')
        if i.isalpha():
            new_str[idx] = i.swapcase()
            flg = 1
        idx += 1
    s = ""
    for i in new_str:
        s += i
    print(f'[ITE][LOC]15[/LOC][VAR]flg == 0[/VAR][VAL]{flg == 0}[/VAL][/ITE]')
    if flg == 0:
        return s[len(s)::-1]
    return s

solve("#a@C")
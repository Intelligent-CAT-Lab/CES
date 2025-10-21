from typing import *


def solve(s):
    flg = 0
    idx = 0
    new_str = list(s)
    print(f'[ITE][LOC]8[/LOC][VAR]s[/VAR][VAL]{s}[/VAL][/ITE]')
    for i in s:
        if i.isalpha():
            new_str[idx] = i.swapcase()
            flg = 1
        idx += 1
    s = ""
    print(f'[ITE][LOC]14[/LOC][VAR]new_str[/VAR][VAL]{new_str}[/VAL][/ITE]')
    for i in new_str:
        s += i
    if flg == 0:
        return s[len(s)::-1]
    return s

solve("ab")
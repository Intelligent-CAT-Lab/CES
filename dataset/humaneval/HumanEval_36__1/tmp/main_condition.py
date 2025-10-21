from typing import *


def fizz_buzz(n: int):
    ns = []
    for i in range(n):
        print(f'[ITE][LOC]6[/LOC][VAR]i % 11 == 0 or i % 13 == 0[/VAR][VAL]{i % 11 == 0 or i % 13 == 0}[/VAL][/ITE]')
        print(f'[ITE][LOC]6[/LOC][VAR]i % 11 == 0[/VAR][VAL]{i % 11 == 0}[/VAL][/ITE]')
        print(f'[ITE][LOC]6[/LOC][VAR]i % 13 == 0[/VAR][VAL]{i % 13 == 0}[/VAL][/ITE]')
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans

fizz_buzz(200)
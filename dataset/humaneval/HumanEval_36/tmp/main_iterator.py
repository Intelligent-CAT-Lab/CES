from typing import *
def fizz_buzz(n: int):
    ns = []
    for i in range(n):
        print(f'[ITE][LOC]4[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        print(f'[ITE][LOC]9[/LOC][VAR]c[/VAR][VAL]{c}[/VAL][/ITE]')
        ans += (c == '7')
    return ans

fizz_buzz(50) 
from typing import *
def fizz_buzz(n: int):
    ns = []
    print(f'[ITE][LOC]4[/LOC][VAR]range(n)[/VAR][VAL]{list(range(n))}[/VAL][/ITE]')
    print(f'[ITE][LOC]4[/LOC][VAR]n[/VAR][VAL]{n}[/VAL][/ITE]')
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    print(f'[ITE][LOC]9[/LOC][VAR]s[/VAR][VAL]{s}[/VAL][/ITE]')
    for c in s:
        ans += (c == '7')
    return ans

fizz_buzz(50) 
from typing import *


def rounded_avg(n, m):
    if m < n:
        return -1
    summation = 0
    print(f'[ITE][LOC]8[/LOC][VAR]range(n, (m + 1))[/VAR][VAL]{list(range(n, (m + 1)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]8[/LOC][VAR]n[/VAR][VAL]{n}[/VAL][/ITE]')
    print(f'[ITE][LOC]8[/LOC][VAR](m + 1)[/VAR][VAL]{(m + 1)}[/VAL][/ITE]')
    for i in range(n, m + 1):
        summation += i
    return bin(round(summation / (m - n + 1)))

rounded_avg(350,902)
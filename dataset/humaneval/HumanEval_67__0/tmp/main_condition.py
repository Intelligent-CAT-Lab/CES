from typing import *


def fruit_distribution(s, n):
    lis = list()
    for i in s.split(' '):
        print(f'[ITE][LOC]6[/LOC][VAR]i.isdigit()[/VAR][VAL]{i.isdigit()}[/VAL][/ITE]')
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)

fruit_distribution("2 apples and 3 oranges",5)
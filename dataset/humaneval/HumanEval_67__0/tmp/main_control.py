from typing import *


def fruit_distribution(s, n):
    lis = list()
    print(f"[ITE][LOC]6[/LOC][VAR]s.split(' ')[/VAR][VAL]{s.split(' ')}[/VAL][/ITE]")
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)

fruit_distribution("2 apples and 3 oranges",5)
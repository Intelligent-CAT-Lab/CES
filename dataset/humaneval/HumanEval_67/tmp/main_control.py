from typing import *
def fruit_distribution(s,n):
    lis = list()
    print(f"[ITE][LOC]4[/LOC][VAR]s.split(' ')[/VAR][VAL]{s.split(' ')}[/VAL][/ITE]")
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)

fruit_distribution("5 apples and 6 oranges",19) 
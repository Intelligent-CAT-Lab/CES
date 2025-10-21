from typing import *


def fruit_distribution(s, n):
    lis = list()
    for i in s.split(' '):
        print('[LINE]6[/LINE] may be hit')
        if i.isdigit():
            print('[LINE]6[/LINE] is hit')
            lis.append(int(i))
    return n - sum(lis)

fruit_distribution("2 apples and 3 oranges",5)
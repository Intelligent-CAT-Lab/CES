from typing import *


def fibfib(n: int):
    print('[LINE]4[/LINE] may be hit')
    if n == 0:
        print('[LINE]4[/LINE] is hit')
        return 0
    print('[LINE]6[/LINE] may be hit')
    if n == 1:
        print('[LINE]6[/LINE] is hit')
        return 0
    print('[LINE]8[/LINE] may be hit')
    if n == 2:
        print('[LINE]8[/LINE] is hit')
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)

fibfib(10)
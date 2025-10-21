from typing import *


def fib(n: int):
    print('[LINE]4[/LINE] may be hit')
    if n == 0:
        print('[LINE]4[/LINE] is hit')
        return 0
    print('[LINE]6[/LINE] may be hit')
    if n == 1:
        print('[LINE]6[/LINE] is hit')
        return 1
    return fib(n - 1) + fib(n - 2)

fib(11)
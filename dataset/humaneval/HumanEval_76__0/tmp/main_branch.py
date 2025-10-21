from typing import *


def is_simple_power(x, n):
    print('[LINE]4[/LINE] may be hit')
    if (n == 1):
        print('[LINE]4[/LINE] is hit')
        return (x == 1)
    power = 1
    while (power < x):
        power = power * n
    return (power == x)

is_simple_power(1, 1)
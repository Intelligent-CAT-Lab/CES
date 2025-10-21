from typing import *


def largest_divisor(n: int) -> int:
    for i in reversed(range(n)):
        print('[LINE]5[/LINE] may be hit')
        if n % i == 0:
            print('[LINE]5[/LINE] is hit')
            return i

largest_divisor(100)
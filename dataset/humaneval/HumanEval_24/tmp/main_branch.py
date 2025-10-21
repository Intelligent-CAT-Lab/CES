from typing import *
def largest_divisor(n: int) -> int:
    for i in reversed(range(n)):
        print('[LINE]3[/LINE] may be hit')
        if n % i == 0:
            print('[LINE]3[/LINE] is hit')
            return i

largest_divisor(3) 
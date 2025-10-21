from typing import *


def is_prime(n):
    print('[LINE]4[/LINE] may be hit')
    if n < 2:
        print('[LINE]4[/LINE] is hit')
        return False
    for k in range(2, n - 1):
        print('[LINE]7[/LINE] may be hit')
        if n % k == 0:
            print('[LINE]7[/LINE] is hit')
            return False
    return True

is_prime(5 * 17)
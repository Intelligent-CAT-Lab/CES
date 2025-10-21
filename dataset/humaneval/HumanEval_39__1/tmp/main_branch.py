from typing import *


def prime_fib(n: int):
    import math

    def is_prime(p):
        print('[LINE]7[/LINE] may be hit')
        if p < 2:
            print('[LINE]7[/LINE] is hit')
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
            print('[LINE]10[/LINE] may be hit')
            if p % k == 0:
                print('[LINE]10[/LINE] is hit')
                return False
        return True
    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        print('[LINE]16[/LINE] may be hit')
        if is_prime(f[-1]):
            print('[LINE]16[/LINE] is hit')
            n -= 1
        print('[LINE]18[/LINE] may be hit')
        if n == 0:
            print('[LINE]18[/LINE] is hit')
            return f[-1]

prime_fib(4)
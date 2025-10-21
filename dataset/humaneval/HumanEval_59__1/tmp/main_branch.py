from typing import *


def largest_prime_factor(n: int):
    def is_prime(k):
        print('[LINE]5[/LINE] may be hit')
        if k < 2:
            print('[LINE]5[/LINE] is hit')
            return False
        for i in range(2, k - 1):
            print('[LINE]8[/LINE] may be hit')
            if k % i == 0:
                print('[LINE]8[/LINE] is hit')
                return False
        return True
    largest = 1
    for j in range(2, n + 1):
        print('[LINE]13[/LINE] may be hit')
        if n % j == 0 and is_prime(j):
            print('[LINE]13[/LINE] is hit')
            largest = max(largest, j)
    return largest

largest_prime_factor(63)
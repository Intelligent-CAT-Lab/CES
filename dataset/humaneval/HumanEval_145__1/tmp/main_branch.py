from typing import *


def order_by_points(nums):
    def digits_sum(n):
        neg = 1
        print('[LINE]6[/LINE] may be hit')
        if n < 0:
            print('[LINE]6[/LINE] is hit')
            n, neg = -1 * n, -1
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)

order_by_points([])
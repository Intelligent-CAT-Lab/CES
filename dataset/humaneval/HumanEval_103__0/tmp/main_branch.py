from typing import *


def rounded_avg(n, m):
    print('[LINE]4[/LINE] may be hit')
    if m < n:
        print('[LINE]4[/LINE] is hit')
        return -1
    summation = 0
    for i in range(n, m + 1):
        summation += i
    return bin(round(summation / (m - n + 1)))

rounded_avg(560,851)
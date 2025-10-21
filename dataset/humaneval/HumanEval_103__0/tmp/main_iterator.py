from typing import *


def rounded_avg(n, m):
    if m < n:
        return -1
    summation = 0
    for i in range(n, m + 1):
        print(f'[ITE][LOC]8[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        summation += i
    return bin(round(summation / (m - n + 1)))

rounded_avg(560,851)
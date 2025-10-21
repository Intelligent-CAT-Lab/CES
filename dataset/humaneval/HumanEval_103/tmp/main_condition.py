from typing import *
def rounded_avg(n, m):
    print(f'[ITE][LOC]2[/LOC][VAR]m < n[/VAR][VAL]{m < n}[/VAL][/ITE]')
    if m < n:
        return -1
    summation = 0
    for i in range(n, m+1):
        summation += i
    return bin(round(summation/(m - n + 1)))

rounded_avg(1, 5) 
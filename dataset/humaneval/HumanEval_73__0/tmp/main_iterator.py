from typing import *


def smallest_change(arr):
    ans = 0
    for i in range(len(arr) // 2):
        print(f'[ITE][LOC]6[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans

smallest_change([1, 4, 2])
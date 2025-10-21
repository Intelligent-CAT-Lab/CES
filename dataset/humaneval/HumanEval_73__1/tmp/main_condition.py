from typing import *


def smallest_change(arr):
    ans = 0
    for i in range(len(arr) // 2):
        print(f'[ITE][LOC]6[/LOC][VAR]arr[i] != arr[len(arr) - i - 1][/VAR][VAL]{arr[i] != arr[len(arr) - i - 1]}[/VAL][/ITE]')
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans

smallest_change([1, 2, 3, 4, 3, 2, 2])
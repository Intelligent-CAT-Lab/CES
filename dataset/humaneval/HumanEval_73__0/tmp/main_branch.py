from typing import *


def smallest_change(arr):
    ans = 0
    for i in range(len(arr) // 2):
        print('[LINE]6[/LINE] may be hit')
        if arr[i] != arr[len(arr) - i - 1]:
            print('[LINE]6[/LINE] is hit')
            ans += 1
    return ans

smallest_change([1, 4, 2])
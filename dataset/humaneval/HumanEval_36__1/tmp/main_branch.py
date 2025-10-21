from typing import *


def fizz_buzz(n: int):
    ns = []
    for i in range(n):
        print('[LINE]6[/LINE] may be hit')
        if i % 11 == 0 or i % 13 == 0:
            print('[LINE]6[/LINE] is hit')
            ns.append(i)
    s = ''.join(list(map(str, ns)))
    ans = 0
    for c in s:
        ans += (c == '7')
    return ans

fizz_buzz(200)
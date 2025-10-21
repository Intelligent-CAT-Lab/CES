from typing import *


def exchange(lst1, lst2):
    odd = 0
    even = 0
    print(f'[ITE][LOC]7[/LOC][VAR]lst1[/VAR][VAL]{lst1}[/VAL][/ITE]')
    for i in lst1:
        if i % 2 == 1:
            odd += 1
    print(f'[ITE][LOC]10[/LOC][VAR]lst2[/VAR][VAL]{lst2}[/VAL][/ITE]')
    for i in lst2:
        if i % 2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"

exchange([3, 2, 6, 1, 8, 9], [3, 5, 5, 1, 1, 1])
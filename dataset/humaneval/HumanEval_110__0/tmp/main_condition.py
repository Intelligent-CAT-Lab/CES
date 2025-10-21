from typing import *


def exchange(lst1, lst2):
    odd = 0
    even = 0
    for i in lst1:
        print(f'[ITE][LOC]7[/LOC][VAR]i % 2 == 1[/VAR][VAL]{i % 2 == 1}[/VAL][/ITE]')
        if i % 2 == 1:
            odd += 1
    for i in lst2:
        print(f'[ITE][LOC]10[/LOC][VAR]i % 2 == 0[/VAR][VAL]{i % 2 == 0}[/VAL][/ITE]')
        if i % 2 == 0:
            even += 1
    print(f'[ITE][LOC]12[/LOC][VAR]even >= odd[/VAR][VAL]{even >= odd}[/VAL][/ITE]')
    if even >= odd:
        return "YES"
    return "NO"

exchange([3, 2, 6, 1, 8, 9], [3, 5, 5, 1, 1, 1])
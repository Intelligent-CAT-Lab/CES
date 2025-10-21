from typing import *
def exchange(lst1, lst2):
    odd = 0
    even = 0
    for i in lst1:
        print(f'[ITE][LOC]5[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if i%2 == 1:
            odd += 1
    for i in lst2:
        print(f'[ITE][LOC]8[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if i%2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"
            

exchange([1, 2, 3, 4], [1, 2, 3, 4]) 
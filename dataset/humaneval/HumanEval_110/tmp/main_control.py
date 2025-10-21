from typing import *
def exchange(lst1, lst2):
    odd = 0
    even = 0
    print(f'[ITE][LOC]5[/LOC][VAR]lst1[/VAR][VAL]{lst1}[/VAL][/ITE]')
    for i in lst1:
        if i%2 == 1:
            odd += 1
    print(f'[ITE][LOC]8[/LOC][VAR]lst2[/VAR][VAL]{lst2}[/VAL][/ITE]')
    for i in lst2:
        if i%2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"
            

exchange([1, 2, 3, 4], [1, 2, 3, 4]) 
from typing import *


def exchange(lst1, lst2):
    odd = 0
    even = 0
    for i in lst1:
        print('[LINE]7[/LINE] may be hit')
        if i % 2 == 1:
            print('[LINE]7[/LINE] is hit')
            odd += 1
    for i in lst2:
        print('[LINE]10[/LINE] may be hit')
        if i % 2 == 0:
            print('[LINE]10[/LINE] is hit')
            even += 1
    print('[LINE]12[/LINE] may be hit')
    if even >= odd:
        print('[LINE]12[/LINE] is hit')
        return "YES"
    return "NO"

exchange([3, 2, 6, 1, 8, 9], [3, 5, 5, 1, 1, 1])
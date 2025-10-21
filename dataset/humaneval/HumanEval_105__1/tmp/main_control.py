from typing import *


def by_length(arr):
    dic = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    sorted_arr = sorted(arr, reverse=True)
    new_arr = []
    print(f'[ITE][LOC]18[/LOC][VAR]sorted_arr[/VAR][VAL]{sorted_arr}[/VAL][/ITE]')
    for var in sorted_arr:
        try:
            new_arr.append(dic[var])
        except BaseException:
            pass
    return new_arr

by_length([])
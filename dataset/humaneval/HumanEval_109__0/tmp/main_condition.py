from typing import *


def move_one_ball(arr):
    print(f'[ITE][LOC]4[/LOC][VAR]len(arr) == 0[/VAR][VAL]{len(arr) == 0}[/VAL][/ITE]')
    if len(arr) == 0:
        return True
    sorted_array = sorted(arr)
    my_arr = []

    min_value = min(arr)
    min_index = arr.index(min_value)
    my_arr = arr[min_index:] + arr[0:min_index]
    for i in range(len(arr)):
        print(f'[ITE][LOC]13[/LOC][VAR]my_arr[i] != sorted_array[i][/VAR][VAL]{my_arr[i] != sorted_array[i]}[/VAL][/ITE]')
        if my_arr[i] != sorted_array[i]:
            return False
    return True

move_one_ball([4, 3, 1, 2])
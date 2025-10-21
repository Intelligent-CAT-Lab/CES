from typing import *


def can_arrange(arr):
    ind = -1
    i = 1
    while i < len(arr):
        print('[LINE]7[/LINE] may be hit')
        if arr[i] < arr[i - 1]:
            print('[LINE]7[/LINE] is hit')
            ind = i
        i += 1
    return ind

can_arrange([4,8,5,7,3])
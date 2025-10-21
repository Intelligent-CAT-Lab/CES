from typing import *


def file_name_check(file_name):
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    print('[LINE]6[/LINE] may be hit')
    if len(lst) != 2:
        print('[LINE]6[/LINE] is hit')
        return 'No'
    print('[LINE]8[/LINE] may be hit')
    if not lst[1] in suf:
        print('[LINE]8[/LINE] is hit')
        return 'No'
    print('[LINE]10[/LINE] may be hit')
    if len(lst[0]) == 0:
        print('[LINE]10[/LINE] is hit')
        return 'No'
    print('[LINE]12[/LINE] may be hit')
    if not lst[0][0].isalpha():
        print('[LINE]12[/LINE] is hit')
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    print('[LINE]15[/LINE] may be hit')
    if t > 3:
        print('[LINE]15[/LINE] is hit')
        return 'No'
    return 'Yes'

file_name_check('@this1_is6_valid.exe')
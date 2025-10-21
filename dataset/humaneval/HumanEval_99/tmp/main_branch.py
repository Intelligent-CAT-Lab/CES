from typing import *
def closest_integer(value):
    from math import floor, ceil

    print('[LINE]4[/LINE] may be hit')
    if value.count('.') == 1:
        print('[LINE]4[/LINE] is hit')
        # remove trailing zeros
        while (value[-1] == '0'):
            value = value[:-1]

    num = float(value)
    print('[LINE]10[/LINE] may be hit')
    print('[LINE]13[/LINE] may be hit')
    print('[LINE]15[/LINE] may be hit')
    print('[LINE]17[/LINE] may be hit')
    if value[-2:] == '.5':
        print('[LINE]10[/LINE] is hit')
        print('[LINE]11[/LINE] may be hit')
        if num > 0:
            print('[LINE]11[/LINE] is hit')
            res = ceil(num)
        else:
            print('[LINE]13[/LINE] is hit')
            res = floor(num)
    elif len(value) > 0:
        print('[LINE]15[/LINE] is hit')
        res = int(round(num))
    else:
        print('[LINE]17[/LINE] is hit')
        res = 0

    return res


closest_integer("10") 
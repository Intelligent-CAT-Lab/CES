def closest_integer(value):
    from math import floor, ceil

    print('[LINE]3[/LINE] may be hit')
    if value.count('.') == 1:
        print('[LINE]3[/LINE] is hit')
        # remove trailing zeros
        while (value[-1] == '0'):
            value = value[:-1]

    num = float(value)
    print('[LINE]9[/LINE] may be hit')
    print('[LINE]12[/LINE] may be hit')
    print('[LINE]14[/LINE] may be hit')
    print('[LINE]16[/LINE] may be hit')
    if value[-2:] == '.5':
        print('[LINE]9[/LINE] is hit')
        print('[LINE]10[/LINE] may be hit')
        if num > 0:
            print('[LINE]10[/LINE] is hit')
            res = floor(num)
        else:
            print('[LINE]12[/LINE] is hit')
            res = ceil(num)
    elif len(value) > 0:
        print('[LINE]14[/LINE] is hit')
        res = int(round(num))
    else:
        print('[LINE]16[/LINE] is hit')
        res = 0

    return res


closest_integer('14.5')
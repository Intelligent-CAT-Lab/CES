def closest_integer(value):
    from math import floor, ceil

    if value.count('.') == 1:
        # remove trailing zeros
        while (value[-1] == '0'):
            print(f"[ITE][LOC]6[/LOC][VAR](value[(- 1)] == '0')[/VAR][VAL]{(value[(- 1)] == '0')}[/VAL][/ITE]")
            print(f'[ITE][LOC]6[/LOC][VAR]value[(- 1)][/VAR][VAL]{value[(- 1)]}[/VAL][/ITE]')
            value = value[:-1]

    num = float(value)
    if value[-2:] == '.5':
        if num > 0:
            res = floor(num)
        else:
            res = ceil(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0

    return res


closest_integer('14.5')

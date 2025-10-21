from typing import *


def closest_integer(value):
    from math import floor, ceil

    print(f"[ITE][LOC]6[/LOC][VAR]value.count('.') == 1[/VAR][VAL]{value.count('.') == 1}[/VAL][/ITE]")
    if value.count('.') == 1:
        # remove trailing zeros
        while (value[-1] == '0'):
            value = value[:-1]

    num = float(value)
    print(f"[ITE][LOC]12[/LOC][VAR]value[-2:] == '.5'[/VAR][VAL]{value[-2:] == '.5'}[/VAL][/ITE]")
    if value[-2:] == '.5':
        print(f'[ITE][LOC]13[/LOC][VAR]num > 0[/VAR][VAL]{num > 0}[/VAL][/ITE]')
        if num > 0:
            res = ceil(num)
        else:
            res = floor(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0

    return res

closest_integer("14.5")
from typing import *
import math

def poly(xs: list, x: float):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    begin, end = -1., 1.
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2.0
        end *= 2.0
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        print('[LINE]13[/LINE] may be hit')
        print('[LINE]15[/LINE] may be hit')
        if poly(xs, center) * poly(xs, begin) > 0:
            print('[LINE]13[/LINE] is hit')
            begin = center
        else:
            print('[LINE]15[/LINE] is hit')
            end = center
    return begin

find_zero([-6, 11, -6, 1])
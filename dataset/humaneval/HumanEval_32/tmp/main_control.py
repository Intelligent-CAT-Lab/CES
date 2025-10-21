from typing import *
import math

def poly(xs: list, x: float):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    begin, end = -1., 1.
    print(f'[ITE][LOC]9[/LOC][VAR]((poly(xs, begin) * poly(xs, end)) > 0)[/VAR][VAL]{((poly(xs, begin) * poly(xs, end)) > 0)}[/VAL][/ITE]')
    print(f'[ITE][LOC]9[/LOC][VAR](poly(xs, begin) * poly(xs, end))[/VAR][VAL]{(poly(xs, begin) * poly(xs, end))}[/VAL][/ITE]')
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2.0
        end *= 2.0
    print(f'[ITE][LOC]12[/LOC][VAR]((end - begin) > 1e-10)[/VAR][VAL]{((end - begin) > 1e-10)}[/VAL][/ITE]')
    print(f'[ITE][LOC]12[/LOC][VAR](end - begin)[/VAR][VAL]{(end - begin)}[/VAL][/ITE]')
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(xs, center) * poly(xs, begin) > 0:
            begin = center
        else:
            end = center
    return begin

find_zero([-6, 11, -6, 1])
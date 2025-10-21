from typing import *


def simplify(x, n):
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    print(f'[ITE][LOC]8[/LOC][VAR]numerator / denom == int(numerator / denom)[/VAR][VAL]{numerator / denom == int(numerator / denom)}[/VAL][/ITE]')
    if (numerator / denom == int(numerator / denom)):
        return True
    return False

simplify("2/4", "8/4")
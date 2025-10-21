from typing import *


def simplify(x, n):
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    print('[LINE]8[/LINE] may be hit')
    if (numerator / denom == int(numerator / denom)):
        print('[LINE]8[/LINE] is hit')
        return True
    return False

simplify("5/1", "3/1")
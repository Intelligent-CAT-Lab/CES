from typing import *


def triangle_area(a, b, c):
    print('[LINE]4[/LINE] may be hit')
    if a + b <= c or a + c <= b or b + c <= a:
        print('[LINE]4[/LINE] is hit')
        return -1
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area

triangle_area(1, 2, 10)
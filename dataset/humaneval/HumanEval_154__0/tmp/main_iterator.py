from typing import *


def cycpattern_check(a, b):
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        print(f'[ITE][LOC]7[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        for j in range(l + 1):
            print(f'[ITE][LOC]8[/LOC][VAR]j[/VAR][VAL]{j}[/VAL][/ITE]')
            if a[i:i + l] == pat[j:j + l]:
                return True
    return False

cycpattern_check("winemtt","tinem")
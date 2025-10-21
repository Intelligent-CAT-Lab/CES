from typing import *


def circular_shift(x, shift):
    s = str(x)
    print(f'[ITE][LOC]5[/LOC][VAR]shift > len(s)[/VAR][VAL]{shift > len(s)}[/VAL][/ITE]')
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]

circular_shift(12, 1)
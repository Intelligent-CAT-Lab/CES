from typing import *


def cycpattern_check(a, b):
    l = len(b)
    pat = b + b
    print(f'[ITE][LOC]7[/LOC][VAR]range(((len(a) - l) + 1))[/VAR][VAL]{list(range(((len(a) - l) + 1)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]7[/LOC][VAR]((len(a) - l) + 1)[/VAR][VAL]{((len(a) - l) + 1)}[/VAL][/ITE]')
    for i in range(len(a) - l + 1):
        print(f'[ITE][LOC]8[/LOC][VAR]range((l + 1))[/VAR][VAL]{list(range((l + 1)))}[/VAL][/ITE]')
        print(f'[ITE][LOC]8[/LOC][VAR](l + 1)[/VAR][VAL]{(l + 1)}[/VAL][/ITE]')
        for j in range(l + 1):
            if a[i:i + l] == pat[j:j + l]:
                return True
    return False

cycpattern_check("efef","fee")
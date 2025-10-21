from typing import *
def cycpattern_check(a , b):
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            print(f'[ITE][LOC]6[/LOC][VAR]a[i:i+l] == pat[j:j+l][/VAR][VAL]{a[i:i+l] == pat[j:j+l]}[/VAL][/ITE]')
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False

cycpattern_check("xyzw","xyw") 
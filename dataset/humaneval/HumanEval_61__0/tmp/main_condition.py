from typing import *


def correct_bracketing(brackets: str):
    depth = 0
    for b in brackets:
        print(f'[ITE][LOC]6[/LOC][VAR]b == "("[/VAR][VAL]{b == "("}[/VAL][/ITE]')
        if b == "(":
            depth += 1
        else:
            depth -= 1
        print(f'[ITE][LOC]10[/LOC][VAR]depth < 0[/VAR][VAL]{depth < 0}[/VAL][/ITE]')
        if depth < 0:
            return False
    return depth == 0

correct_bracketing(")((")
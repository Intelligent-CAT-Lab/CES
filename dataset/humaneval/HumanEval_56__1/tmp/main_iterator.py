from typing import *


def correct_bracketing(brackets: str):
    depth = 0
    for b in brackets:
        print(f'[ITE][LOC]6[/LOC][VAR]b[/VAR][VAL]{b}[/VAL][/ITE]')
        if b == "<":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0

correct_bracketing("<<<><>>>>")
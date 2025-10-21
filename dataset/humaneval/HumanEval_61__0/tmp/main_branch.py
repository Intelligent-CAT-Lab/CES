from typing import *


def correct_bracketing(brackets: str):
    depth = 0
    for b in brackets:
        print('[LINE]6[/LINE] may be hit')
        print('[LINE]8[/LINE] may be hit')
        if b == "(":
            print('[LINE]6[/LINE] is hit')
            depth += 1
        else:
            print('[LINE]8[/LINE] is hit')
            depth -= 1
        print('[LINE]10[/LINE] may be hit')
        if depth < 0:
            print('[LINE]10[/LINE] is hit')
            return False
    return depth == 0

correct_bracketing(")((")
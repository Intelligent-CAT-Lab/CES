def correct_bracketing(brackets: str):
    depth = 0
    print(f'[ITE][LOC]3[/LOC][VAR]brackets[/VAR][VAL]{brackets}[/VAL][/ITE]')
    for b in brackets:
        if b == ">":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0

correct_bracketing('<<><>>')

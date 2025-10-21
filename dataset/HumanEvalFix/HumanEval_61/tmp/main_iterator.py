def correct_bracketing(brackets: str):
    depth = 0
    for b in brackets:
        print(f'[ITE][LOC]3[/LOC][VAR]b[/VAR][VAL]{b}[/VAL][/ITE]')
        if b == "(":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return True
    return depth == 0

correct_bracketing('((()())))')

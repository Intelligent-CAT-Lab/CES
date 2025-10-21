def below_threshold(l: list, t: int):
    for e in l:
        print(f'[ITE][LOC]2[/LOC][VAR]e[/VAR][VAL]{e}[/VAL][/ITE]')
        if e >= t:
            return True
    return False

below_threshold([1, 20, 4, 10], 21)

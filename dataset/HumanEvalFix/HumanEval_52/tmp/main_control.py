def below_threshold(l: list, t: int):
    print(f'[ITE][LOC]2[/LOC][VAR]l[/VAR][VAL]{l}[/VAL][/ITE]')
    for e in l:
        if e >= t:
            return True
    return False

below_threshold([1, 20, 4, 10], 21)

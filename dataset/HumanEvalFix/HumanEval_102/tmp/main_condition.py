def choose_num(x, y):
    print(f'[ITE][LOC]1[/LOC][VAR]x > y[/VAR][VAL]{x > y}[/VAL][/ITE]')
    if x > y:
        return -1
    print(f'[ITE][LOC]3[/LOC][VAR]y % 2 == 0[/VAR][VAL]{y % 2 == 0}[/VAL][/ITE]')
    if y % 2 == 0:
        return y
    print(f'[ITE][LOC]5[/LOC][VAR]x == y[/VAR][VAL]{x == y}[/VAL][/ITE]')
    if x == y:
        return -1
    return x - 1

choose_num(12, 15)

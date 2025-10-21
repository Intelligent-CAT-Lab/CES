def change_base(x: int, base: int):
    ret = ""
    while x > 0:
        print(f'[ITE][LOC]3[/LOC][VAR](x > 0)[/VAR][VAL]{(x > 0)}[/VAL][/ITE]')
        print(f'[ITE][LOC]3[/LOC][VAR]x[/VAR][VAL]{x}[/VAL][/ITE]')
        ret = str(x % base) + ret
        x -= base
    return ret

change_base(8, 3)

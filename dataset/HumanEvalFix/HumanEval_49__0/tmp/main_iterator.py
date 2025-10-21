def modp(n: int, p: int):
    ret = 0
    for i in range(n):
        print(f'[ITE][LOC]3[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        ret = (2 * ret) % p
    return ret

modp(3, 11)

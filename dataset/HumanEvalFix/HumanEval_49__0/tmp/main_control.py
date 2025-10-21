def modp(n: int, p: int):
    ret = 0
    print(f'[ITE][LOC]3[/LOC][VAR]range(n)[/VAR][VAL]{list(range(n))}[/VAL][/ITE]')
    print(f'[ITE][LOC]3[/LOC][VAR]n[/VAR][VAL]{n}[/VAL][/ITE]')
    for i in range(n):
        ret = (2 * ret) % p
    return ret

modp(3, 11)

def simplify(x, n):
    a, b = x.split("/")
    c, d = n.split("/")
    a = int(b) * int(c)
    d = int(c) * int(b)
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    print(f'[ITE][LOC]7[/LOC][VAR]numerator/denom == int(numerator/denom)[/VAR][VAL]{numerator/denom == int(numerator/denom)}[/VAL][/ITE]')
    if (numerator/denom == int(numerator/denom)):
        return True
    return False

simplify('7/10', '10/2')

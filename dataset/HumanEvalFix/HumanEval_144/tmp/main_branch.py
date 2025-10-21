def simplify(x, n):
    a, b = x.split("/")
    c, d = n.split("/")
    a = int(b) * int(c)
    d = int(c) * int(b)
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    print('[LINE]7[/LINE] may be hit')
    if (numerator/denom == int(numerator/denom)):
        print('[LINE]7[/LINE] is hit')
        return True
    return False

simplify('7/10', '10/2')
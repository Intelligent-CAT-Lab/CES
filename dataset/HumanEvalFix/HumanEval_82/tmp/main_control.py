def prime_length(string):
    l = len(string)
    if l == 0 or l == 1:
        return False
    print(f'[ITE][LOC]5[/LOC][VAR]range(3, l)[/VAR][VAL]{list(range(3, l))}[/VAL][/ITE]')
    print(f'[ITE][LOC]5[/LOC][VAR]l[/VAR][VAL]{l}[/VAL][/ITE]')
    for i in range(3, l):
        if l % i == 0:
            return False
    return True

prime_length('gogo')

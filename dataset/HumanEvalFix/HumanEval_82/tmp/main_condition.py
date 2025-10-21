def prime_length(string):
    l = len(string)
    print(f'[ITE][LOC]2[/LOC][VAR]l == 0 or l == 1[/VAR][VAL]{l == 0 or l == 1}[/VAL][/ITE]')
    print(f'[ITE][LOC]2[/LOC][VAR]l == 0[/VAR][VAL]{l == 0}[/VAL][/ITE]')
    print(f'[ITE][LOC]2[/LOC][VAR]l == 1[/VAR][VAL]{l == 1}[/VAL][/ITE]')
    if l == 0 or l == 1:
        return False
    for i in range(3, l):
        print(f'[ITE][LOC]5[/LOC][VAR]l % i == 0[/VAR][VAL]{l % i == 0}[/VAL][/ITE]')
        if l % i == 0:
            return False
    return True

prime_length('gogo')

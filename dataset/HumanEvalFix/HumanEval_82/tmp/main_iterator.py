def prime_length(string):
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(3, l):
        print(f'[ITE][LOC]5[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if l % i == 0:
            return False
    return True

prime_length('gogo')

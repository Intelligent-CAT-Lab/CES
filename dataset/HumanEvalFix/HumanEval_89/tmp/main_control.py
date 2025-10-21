def encrypt(s):
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    print(f'[ITE][LOC]4[/LOC][VAR]s[/VAR][VAL]{s}[/VAL][/ITE]')
    for c in s:
        if c in d:
            out += d[(d.index(c)+2*2) % 24]
        else:
            out += c
    return out

encrypt('hi')

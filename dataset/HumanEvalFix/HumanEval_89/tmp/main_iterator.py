def encrypt(s):
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        print(f'[ITE][LOC]4[/LOC][VAR]c[/VAR][VAL]{c}[/VAL][/ITE]')
        if c in d:
            out += d[(d.index(c)+2*2) % 24]
        else:
            out += c
    return out

encrypt('hi')

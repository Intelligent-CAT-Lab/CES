def encrypt(s):
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        print(f'[ITE][LOC]4[/LOC][VAR]c in d[/VAR][VAL]{c in d}[/VAL][/ITE]')
        if c in d:
            out += d[(d.index(c)+2*2) % 24]
        else:
            out += c
    return out

encrypt('hi')

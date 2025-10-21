def encrypt(s):
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        print('[LINE]4[/LINE] may be hit')
        print('[LINE]6[/LINE] may be hit')
        if c in d:
            print('[LINE]4[/LINE] is hit')
            out += d[(d.index(c)+2*2) % 24]
        else:
            print('[LINE]6[/LINE] is hit')
            out += c
    return out

encrypt('hi')
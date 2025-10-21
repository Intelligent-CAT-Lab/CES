from typing import *


def encrypt(s):
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        print('[LINE]7[/LINE] may be hit')
        print('[LINE]9[/LINE] may be hit')
        if c in d:
            print('[LINE]7[/LINE] is hit')
            out += d[(d.index(c) + 2 * 2) % 26]
        else:
            print('[LINE]9[/LINE] is hit')
            out += c
    return out

encrypt('et')
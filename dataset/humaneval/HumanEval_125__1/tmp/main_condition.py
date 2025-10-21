from typing import *


def split_words(txt):
    print(f'[ITE][LOC]4[/LOC][VAR]" " in txt[/VAR][VAL]{" " in txt}[/VAL][/ITE]')
    if " " in txt:
        return txt.split()
    elif "," in txt:
        return txt.replace(',', ' ').split()
    else:
        return len([i for i in txt if i.islower() and ord(i) % 2 == 0])

split_words("Hello world,!")
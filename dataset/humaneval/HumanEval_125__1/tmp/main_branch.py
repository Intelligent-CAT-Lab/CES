from typing import *


def split_words(txt):
    print('[LINE]4[/LINE] may be hit')
    print('[LINE]6[/LINE] may be hit')
    print('[LINE]8[/LINE] may be hit')
    if " " in txt:
        print('[LINE]4[/LINE] is hit')
        return txt.split()
    elif "," in txt:
        print('[LINE]6[/LINE] is hit')
        return txt.replace(',', ' ').split()
    else:
        print('[LINE]8[/LINE] is hit')
        return len([i for i in txt if i.islower() and ord(i) % 2 == 0])

split_words("Hello world,!")
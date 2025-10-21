from typing import *
def words_string(s):
    if not s:
        return []

    s_list = []

    print(f'[ITE][LOC]8[/LOC][VAR]s[/VAR][VAL]{s}[/VAL][/ITE]')
    for letter in s:
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()

words_string("Hi, my name is John") 
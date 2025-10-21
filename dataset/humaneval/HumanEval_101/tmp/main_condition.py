from typing import *
def words_string(s):
    print(f'[ITE][LOC]2[/LOC][VAR]not s[/VAR][VAL]{not s}[/VAL][/ITE]')
    if not s:
        return []

    s_list = []

    for letter in s:
        print(f"[ITE][LOC]8[/LOC][VAR]letter == ','[/VAR][VAL]{letter == ','}[/VAL][/ITE]")
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()

words_string("Hi, my name is John") 
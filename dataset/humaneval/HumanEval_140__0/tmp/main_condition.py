from typing import *


def fix_spaces(text):
    new_text = ""
    i = 0
    start, end = 0, 0
    while i < len(text):
        print(f'[ITE][LOC]8[/LOC][VAR]text[i] == " "[/VAR][VAL]{text[i] == " "}[/VAL][/ITE]')
        if text[i] == " ":
            end += 1
        else:
            print(f'[ITE][LOC]11[/LOC][VAR]end - start > 2[/VAR][VAL]{end - start > 2}[/VAL][/ITE]')
            if end - start > 2:
                new_text += "-" + text[i]
            elif end - start > 0:
                new_text += "_" * (end - start) + text[i]
            else:
                new_text += text[i]
            start, end = i + 1, i + 1
        i += 1
    print(f'[ITE][LOC]19[/LOC][VAR]end - start > 2[/VAR][VAL]{end - start > 2}[/VAL][/ITE]')
    if end - start > 2:
        new_text += "-"
    elif end - start > 0:
        new_text += "_"
    return new_text

fix_spaces("Exa   mple")
from typing import *
def fix_spaces(text):
    new_text = ""
    i = 0
    start, end = 0, 0
    print(f'[ITE][LOC]6[/LOC][VAR](i < len(text))[/VAR][VAL]{(i < len(text))}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR]len(text)[/VAR][VAL]{len(text)}[/VAL][/ITE]')
    while i < len(text):
        if text[i] == " ":
            end += 1
        else:
            if end - start > 2:
                new_text += "-"+text[i]
            elif end - start > 0:
                new_text += "_"*(end - start)+text[i]
            else:
                new_text += text[i]
            start, end = i+1, i+1
        i+=1
    if end - start > 2:
        new_text += "-"
    elif end - start > 0:
        new_text += "_"
    return new_text

fix_spaces("Example") 
from typing import *
def is_palindrome(text: str):
    print(f'[ITE][LOC]3[/LOC][VAR]range(len(text))[/VAR][VAL]{list(range(len(text)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]3[/LOC][VAR]len(text)[/VAR][VAL]{len(text)}[/VAL][/ITE]')
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True

is_palindrome('xywyx') 
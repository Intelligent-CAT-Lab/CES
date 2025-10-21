from typing import *


def is_palindrome(text: str):
    for i in range(len(text)):
        print(f'[ITE][LOC]5[/LOC][VAR]text[i] != text[len(text) - 1 - i][/VAR][VAL]{text[i] != text[len(text) - 1 - i]}[/VAL][/ITE]')
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True

is_palindrome('aaaaa')
from typing import *

def is_palindrome(string: str) -> bool:
    print(f'[ITE][LOC]3[/LOC][VAR]not string[/VAR][VAL]{not string}[/VAL][/ITE]')
    if not string:
        return ''

    beginning_of_suffix = 0

    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]

is_palindrome('jerry') 
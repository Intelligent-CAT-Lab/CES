from typing import *


def is_palindrome(string: str) -> bool:
    if not string:
        return ''

    beginning_of_suffix = 0

    print(f'[ITE][LOC]10[/LOC][VAR](not is_palindrome(string[beginning_of_suffix:]))[/VAR][VAL]{(not is_palindrome(string[beginning_of_suffix:]))}[/VAL][/ITE]')
    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]

is_palindrome('xyx')
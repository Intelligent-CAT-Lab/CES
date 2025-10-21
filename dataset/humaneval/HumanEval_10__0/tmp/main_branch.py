from typing import *


def is_palindrome(string: str) -> bool:
    print('[LINE]4[/LINE] may be hit')
    if not string:
        print('[LINE]4[/LINE] is hit')
        return ''

    beginning_of_suffix = 0

    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]

is_palindrome('xyx')
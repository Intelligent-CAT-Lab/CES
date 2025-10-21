from typing import *
def is_palindrome(text: str):
    for i in range(len(text)):
        print('[LINE]3[/LINE] may be hit')
        if text[i] != text[len(text) - 1 - i]:
            print('[LINE]3[/LINE] is hit')
            return False
    return True

is_palindrome('xywyx') 
from typing import *


def digitSum(s):
    print('[LINE]4[/LINE] may be hit')
    if s == "":
        print('[LINE]4[/LINE] is hit')
        return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)

digitSum("abcCd")
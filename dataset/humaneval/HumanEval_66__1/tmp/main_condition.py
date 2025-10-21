from typing import *


def digitSum(s):
    print(f'[ITE][LOC]4[/LOC][VAR]s == ""[/VAR][VAL]{s == ""}[/VAL][/ITE]')
    if s == "":
        return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)

digitSum("aAaaaXa")
from typing import *


def how_many_times(string: str, substring: str) -> int:
    times = 0

    for i in range(len(string) - len(substring) + 1):
        print(f'[ITE][LOC]7[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if string[i:i + len(substring)] == substring:
            times += 1

    return times

how_many_times('john doe', 'john')
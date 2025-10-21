from typing import *


def how_many_times(string: str, substring: str) -> int:
    times = 0

    print(f'[ITE][LOC]7[/LOC][VAR]range(((len(string) - len(substring)) + 1))[/VAR][VAL]{list(range(((len(string) - len(substring)) + 1)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]7[/LOC][VAR]((len(string) - len(substring)) + 1)[/VAR][VAL]{((len(string) - len(substring)) + 1)}[/VAL][/ITE]')
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            times += 1

    return times

how_many_times('xyxyxyx', 'x')
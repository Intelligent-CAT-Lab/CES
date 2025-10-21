from typing import *


def how_many_times(string: str, substring: str) -> int:
    times = 0

    for i in range(len(string) - len(substring) + 1):
        print('[LINE]7[/LINE] may be hit')
        if string[i:i + len(substring)] == substring:
            print('[LINE]7[/LINE] is hit')
            times += 1

    return times

how_many_times('xyxyxyx', 'x')
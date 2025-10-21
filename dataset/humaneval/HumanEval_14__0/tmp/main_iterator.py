from typing import *


def all_prefixes(string: str) -> List[str]:
    result = []

    for i in range(len(string)):
        print(f'[ITE][LOC]7[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        result.append(string[:i + 1])
    return result

all_prefixes('WWW')
from typing import *


def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    print(f'[ITE][LOC]9[/LOC][VAR]strings[/VAR][VAL]{strings}[/VAL][/ITE]')
    for s in strings:
        if len(s) == maxlen:
            return s

longest(['x', 'y', 'z'])
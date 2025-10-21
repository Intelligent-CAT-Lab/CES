from typing import *


def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        print(f'[ITE][LOC]9[/LOC][VAR]s[/VAR][VAL]{s}[/VAL][/ITE]')
        if len(s) == maxlen:
            return s

longest([])
from typing import *


def longest(strings: List[str]) -> Optional[str]:
    print(f'[ITE][LOC]4[/LOC][VAR]not strings[/VAR][VAL]{not strings}[/VAL][/ITE]')
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        print(f'[ITE][LOC]9[/LOC][VAR]len(s) == maxlen[/VAR][VAL]{len(s) == maxlen}[/VAL][/ITE]')
        if len(s) == maxlen:
            return s

longest(['x', 'y', 'z'])
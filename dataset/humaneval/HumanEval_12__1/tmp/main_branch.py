from typing import *


def longest(strings: List[str]) -> Optional[str]:
    print('[LINE]4[/LINE] may be hit')
    if not strings:
        print('[LINE]4[/LINE] is hit')
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        print('[LINE]9[/LINE] may be hit')
        if len(s) == maxlen:
            print('[LINE]9[/LINE] is hit')
            return s

longest([])
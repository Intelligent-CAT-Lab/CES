from typing import *
def longest(strings: List[str]) -> Optional[str]:
    print('[LINE]2[/LINE] may be hit')
    if not strings:
        print('[LINE]2[/LINE] is hit')
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        print('[LINE]7[/LINE] may be hit')
        if len(s) == maxlen:
            print('[LINE]7[/LINE] is hit')
            return s

longest(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) 
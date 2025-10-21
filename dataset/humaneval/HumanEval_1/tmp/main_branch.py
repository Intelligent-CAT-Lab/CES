from typing import *
from typing import *
def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_string = []
    current_depth = 0

    for c in paren_string:
        print('[LINE]8[/LINE] may be hit')
        print('[LINE]11[/LINE] may be hit')
        if c == '(':
            print('[LINE]8[/LINE] is hit')
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            print('[LINE]11[/LINE] is hit')
            current_depth -= 1
            current_string.append(c)

            print('[LINE]15[/LINE] may be hit')
            if current_depth == 0:
                print('[LINE]15[/LINE] is hit')
                result.append(''.join(current_string))
                current_string.clear()

    return result

separate_paren_groups('(()()) ((())) () ((())()())') 
from typing import *
from typing import *
def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_string = []
    current_depth = 0

    print(f'[ITE][LOC]8[/LOC][VAR]paren_string[/VAR][VAL]{paren_string}[/VAL][/ITE]')
    for c in paren_string:
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            current_string.append(c)

            if current_depth == 0:
                result.append(''.join(current_string))
                current_string.clear()

    return result

separate_paren_groups('(()()) ((())) () ((())()())') 
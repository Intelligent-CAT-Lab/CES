from typing import *
from typing import *
def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    current_string = []
    current_depth = 0

    for c in paren_string:
        print(f"[ITE][LOC]8[/LOC][VAR]c == '('[/VAR][VAL]{c == '('}[/VAL][/ITE]")
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            current_string.append(c)

            print(f'[ITE][LOC]15[/LOC][VAR]current_depth == 0[/VAR][VAL]{current_depth == 0}[/VAL][/ITE]')
            if current_depth == 0:
                result.append(''.join(current_string))
                current_string.clear()

    return result

separate_paren_groups('(()()) ((())) () ((())()())') 
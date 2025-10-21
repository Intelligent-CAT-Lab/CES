from typing import *


def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            print(f"[ITE][LOC]8[/LOC][VAR]c == '('[/VAR][VAL]{c == '('}[/VAL][/ITE]")
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                depth -= 1

        return max_depth

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]

parse_nested_parens('(()(())((())))')
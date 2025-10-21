from typing import *


def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            print('[LINE]8[/LINE] may be hit')
            print('[LINE]11[/LINE] may be hit')
            if c == '(':
                print('[LINE]8[/LINE] is hit')
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                print('[LINE]11[/LINE] is hit')
                depth -= 1

        return max_depth

    return [parse_paren_group(x) for x in paren_string.split(' ') if x]

parse_nested_parens('((()))')
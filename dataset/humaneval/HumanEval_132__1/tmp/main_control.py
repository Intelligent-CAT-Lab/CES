from typing import *


def is_nested(string):
    opening_bracket_index = []
    closing_bracket_index = []
    print(f'[ITE][LOC]7[/LOC][VAR]range(len(string))[/VAR][VAL]{list(range(len(string)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]7[/LOC][VAR]len(string)[/VAR][VAL]{len(string)}[/VAL][/ITE]')
    for i in range(len(string)):
        if string[i] == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    print(f'[ITE][LOC]16[/LOC][VAR]opening_bracket_index[/VAR][VAL]{opening_bracket_index}[/VAL][/ITE]')
    for idx in opening_bracket_index:
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
    return cnt >= 2

is_nested('[[[[]]]]')
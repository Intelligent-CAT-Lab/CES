from typing import *


def is_nested(string):
    opening_bracket_index = []
    closing_bracket_index = []
    for i in range(len(string)):
        print('[LINE]7[/LINE] may be hit')
        print('[LINE]9[/LINE] may be hit')
        if string[i] == '[':
            print('[LINE]7[/LINE] is hit')
            opening_bracket_index.append(i)
        else:
            print('[LINE]9[/LINE] is hit')
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx in opening_bracket_index:
        print('[LINE]16[/LINE] may be hit')
        if i < l and idx < closing_bracket_index[i]:
            print('[LINE]16[/LINE] is hit')
            cnt += 1
            i += 1
    return cnt >= 2

is_nested('[[[[]]]]')
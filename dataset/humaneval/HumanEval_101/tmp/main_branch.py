from typing import *
def words_string(s):
    print('[LINE]2[/LINE] may be hit')
    if not s:
        print('[LINE]2[/LINE] is hit')
        return []

    s_list = []

    for letter in s:
        print('[LINE]8[/LINE] may be hit')
        print('[LINE]10[/LINE] may be hit')
        if letter == ',':
            print('[LINE]8[/LINE] is hit')
            s_list.append(' ')
        else:
            print('[LINE]10[/LINE] is hit')
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()

words_string("Hi, my name is John") 
from typing import *


def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        print('[LINE]5[/LINE] may be hit')
        print('[LINE]7[/LINE] may be hit')
        if i == j:
            print('[LINE]5[/LINE] is hit')
            return '0'
        else:
            print('[LINE]7[/LINE] is hit')
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))

string_xor('0101', '0000')
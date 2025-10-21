from typing import *
def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        print('[LINE]3[/LINE] may be hit')
        print('[LINE]5[/LINE] may be hit')
        if i == j:
            print('[LINE]3[/LINE] is hit')
            return '0'
        else:
            print('[LINE]5[/LINE] is hit')
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))

string_xor('111000', '101010') 
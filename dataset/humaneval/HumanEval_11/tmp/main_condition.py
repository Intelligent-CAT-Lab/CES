from typing import *
def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        print(f'[ITE][LOC]3[/LOC][VAR]i == j[/VAR][VAL]{i == j}[/VAL][/ITE]')
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))

string_xor('111000', '101010') 
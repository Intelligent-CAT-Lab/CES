from typing import List


def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        print(f'[ITE][LOC]5[/LOC][VAR]i == j[/VAR][VAL]{i == j}[/VAL][/ITE]')
        if i == j:
            return '1'
        else:
            return '0'

    return ''.join(xor(x, y) for x, y in zip(a, b))

string_xor('0101', '0000')

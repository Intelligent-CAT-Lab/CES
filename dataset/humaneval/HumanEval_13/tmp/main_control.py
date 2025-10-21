from typing import *
def greatest_common_divisor(a: int, b: int) -> int:
    print(f'[ITE][LOC]3[/LOC][VAR]b[/VAR][VAL]{b}[/VAL][/ITE]')
    while b:
        a, b = b, a % b
    return a

greatest_common_divisor(3, 7) 
from typing import *


def below_zero(operations: List[int]) -> bool:
    balance = 0

    for op in operations:
        balance += op
        print(f'[ITE][LOC]8[/LOC][VAR]balance < 0[/VAR][VAL]{balance < 0}[/VAL][/ITE]')
        if balance < 0:
            return True

    return False

below_zero([1, -1, 2, -2, 5, -5, 4, -4])
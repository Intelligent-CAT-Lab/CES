from typing import *


def below_zero(operations: List[int]) -> bool:
    balance = 0

    for op in operations:
        print(f'[ITE][LOC]7[/LOC][VAR]op[/VAR][VAL]{op}[/VAL][/ITE]')
        balance += op
        if balance < 0:
            return True

    return False

below_zero([1, -1, 2, -2, 5, -5, 4, -4])
from typing import *
def below_zero(operations: List[int]) -> bool:
    balance = 0

    for op in operations:
        balance += op
        print('[LINE]6[/LINE] may be hit')
        if balance < 0:
            print('[LINE]6[/LINE] is hit')
            return True

    return False

below_zero([1, 2, -3, 1, 2, -3]) 
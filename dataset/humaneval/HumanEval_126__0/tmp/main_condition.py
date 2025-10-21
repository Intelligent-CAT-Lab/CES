from typing import *


def is_sorted(lst):
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i] += 1
    print(f'[ITE][LOC]7[/LOC][VAR]any(count_digit[i] > 2 for i in lst)[/VAR][VAL]{any(count_digit[i] > 2 for i in lst)}[/VAL][/ITE]')
    if any(count_digit[i] > 2 for i in lst):
        return False
    print(f'[ITE][LOC]9[/LOC][VAR]all(lst[i - 1] <= lst[i] for i in range(1, len(lst)))[/VAR][VAL]{all(lst[i - 1] <= lst[i] for i in range(1, len(lst)))}[/VAL][/ITE]')
    if all(lst[i - 1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return False

is_sorted([1, 2, 3, 4])
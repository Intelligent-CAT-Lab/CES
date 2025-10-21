from typing import *


def compare_one(a, b):
    temp_a, temp_b = a, b
    print(f'[ITE][LOC]5[/LOC][VAR]isinstance(temp_a, str)[/VAR][VAL]{isinstance(temp_a, str)}[/VAL][/ITE]')
    if isinstance(temp_a, str):
        temp_a = temp_a.replace(',', '.')
    print(f'[ITE][LOC]7[/LOC][VAR]isinstance(temp_b, str)[/VAR][VAL]{isinstance(temp_b, str)}[/VAL][/ITE]')
    if isinstance(temp_b, str):
        temp_b = temp_b.replace(',', '.')
    print(f'[ITE][LOC]9[/LOC][VAR]float(temp_a) == float(temp_b)[/VAR][VAL]{float(temp_a) == float(temp_b)}[/VAL][/ITE]')
    if float(temp_a) == float(temp_b):
        return None
    return a if float(temp_a) > float(temp_b) else b

compare_one(5, 6)
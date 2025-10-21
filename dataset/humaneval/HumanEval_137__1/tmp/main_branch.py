from typing import *


def compare_one(a, b):
    temp_a, temp_b = a, b
    print('[LINE]5[/LINE] may be hit')
    if isinstance(temp_a, str):
        print('[LINE]5[/LINE] is hit')
        temp_a = temp_a.replace(',', '.')
    print('[LINE]7[/LINE] may be hit')
    if isinstance(temp_b, str):
        print('[LINE]7[/LINE] is hit')
        temp_b = temp_b.replace(',', '.')
    print('[LINE]9[/LINE] may be hit')
    if float(temp_a) == float(temp_b):
        print('[LINE]9[/LINE] is hit')
        return None
    return a if float(temp_a) > float(temp_b) else b

compare_one("1", "2")
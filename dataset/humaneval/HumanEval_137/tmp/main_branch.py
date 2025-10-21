from typing import *
def compare_one(a, b):
    temp_a, temp_b = a, b
    print('[LINE]3[/LINE] may be hit')
    if isinstance(temp_a, str): temp_a = temp_a.replace(',','.')
        print('[LINE]3[/LINE] is hit')
    print('[LINE]4[/LINE] may be hit')
    if isinstance(temp_b, str): temp_b = temp_b.replace(',','.')
        print('[LINE]4[/LINE] is hit')
    print('[LINE]5[/LINE] may be hit')
    if float(temp_a) == float(temp_b): return None
        print('[LINE]5[/LINE] is hit')
    return a if float(temp_a) > float(temp_b) else b 

compare_one(1, 2) 
from typing import *


def digits(n):
    product = 1
    odd_count = 0
    for digit in str(n):
        int_digit = int(digit)
        print('[LINE]8[/LINE] may be hit')
        if int_digit % 2 == 1:
            print('[LINE]8[/LINE] is hit')
            product = product * int_digit
            odd_count += 1
    print('[LINE]11[/LINE] may be hit')
    print('[LINE]13[/LINE] may be hit')
    if odd_count == 0:
        print('[LINE]11[/LINE] is hit')
        return 0
    else:
        print('[LINE]13[/LINE] is hit')
        return product

digits(5576543)
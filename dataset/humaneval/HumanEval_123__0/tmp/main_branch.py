from typing import *


def get_odd_collatz(n):
    print('[LINE]4[/LINE] may be hit')
    print('[LINE]6[/LINE] may be hit')
    if n % 2 == 0:
        print('[LINE]4[/LINE] is hit')
        odd_collatz = []
    else:
        print('[LINE]6[/LINE] is hit')
        odd_collatz = [n]
    while n > 1:
        print('[LINE]9[/LINE] may be hit')
        print('[LINE]11[/LINE] may be hit')
        if n % 2 == 0:
            print('[LINE]9[/LINE] is hit')
            n = n / 2
        else:
            print('[LINE]11[/LINE] is hit')
            n = n * 3 + 1

        print('[LINE]14[/LINE] may be hit')
        if n % 2 == 1:
            print('[LINE]14[/LINE] is hit')
            odd_collatz.append(int(n))

    return sorted(odd_collatz)

get_odd_collatz(1)
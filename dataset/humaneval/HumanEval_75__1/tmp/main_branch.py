from typing import *


def is_multiply_prime(a):
    def is_prime(n):
        for j in range(2, n):
            print('[LINE]6[/LINE] may be hit')
            if n % j == 0:
                print('[LINE]6[/LINE] is hit')
                return False
        return True

    for i in range(2, 101):
        print('[LINE]11[/LINE] may be hit')
        if not is_prime(i):
            print('[LINE]11[/LINE] is hit')
            continue
        for j in range(2, 101):
            print('[LINE]14[/LINE] may be hit')
            if not is_prime(j):
                print('[LINE]14[/LINE] is hit')
                continue
            for k in range(2, 101):
                print('[LINE]17[/LINE] may be hit')
                if not is_prime(k):
                    print('[LINE]17[/LINE] is hit')
                    continue
                print('[LINE]19[/LINE] may be hit')
                if i * j * k == a:
                    print('[LINE]19[/LINE] is hit')
                    return True
    return False

is_multiply_prime(125)
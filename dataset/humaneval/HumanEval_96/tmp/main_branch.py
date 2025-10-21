from typing import *
def count_up_to(n):
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            print('[LINE]6[/LINE] may be hit')
            if i % j == 0:
                print('[LINE]6[/LINE] is hit')
                is_prime = False
                break
        print('[LINE]9[/LINE] may be hit')
        if is_prime:
            print('[LINE]9[/LINE] is hit')
            primes.append(i)
    return primes


count_up_to(5) 
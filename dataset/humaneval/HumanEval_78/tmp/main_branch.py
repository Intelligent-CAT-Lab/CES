from typing import *
def hex_key(num):
    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    for i in range(0, len(num)):
        print('[LINE]5[/LINE] may be hit')
        if num[i] in primes:
            print('[LINE]5[/LINE] is hit')
            total += 1
    return total

hex_key("AB") 
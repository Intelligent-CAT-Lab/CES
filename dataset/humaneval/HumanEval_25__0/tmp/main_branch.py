from typing import *


def factorize(n: int) -> List[int]:
    import math
    fact = []
    i = 2
    while i <= int(math.sqrt(n) + 1):
        print('[LINE]8[/LINE] may be hit')
        print('[LINE]11[/LINE] may be hit')
        if n % i == 0:
            print('[LINE]8[/LINE] is hit')
            fact.append(i)
            n //= i
        else:
            print('[LINE]11[/LINE] is hit')
            i += 1

    print('[LINE]14[/LINE] may be hit')
    if n > 1:
        print('[LINE]14[/LINE] is hit')
        fact.append(n)
    return fact

factorize(3 * 2 * 3)
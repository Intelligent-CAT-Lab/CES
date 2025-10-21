from typing import *
def factorize(n: int) -> List[int]:
    import math
    fact = []
    i = 2
    while i <= int(math.sqrt(n) + 1):
        print(f'[ITE][LOC]6[/LOC][VAR]n % i == 0[/VAR][VAL]{n % i == 0}[/VAL][/ITE]')
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1

    print(f'[ITE][LOC]12[/LOC][VAR]n > 1[/VAR][VAL]{n > 1}[/VAL][/ITE]')
    if n > 1:
        fact.append(n)
    return fact

factorize(2) 
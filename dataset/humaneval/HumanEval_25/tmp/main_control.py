from typing import *
def factorize(n: int) -> List[int]:
    import math
    fact = []
    i = 2
    print(f'[ITE][LOC]6[/LOC][VAR](i <= int((math.sqrt(n) + 1)))[/VAR][VAL]{(i <= int((math.sqrt(n) + 1)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR]int((math.sqrt(n) + 1))[/VAR][VAL]{int((math.sqrt(n) + 1))}[/VAL][/ITE]')
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        fact.append(n)
    return fact

factorize(2) 
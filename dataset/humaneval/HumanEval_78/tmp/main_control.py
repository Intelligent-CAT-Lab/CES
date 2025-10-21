from typing import *
def hex_key(num):
    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    print(f'[ITE][LOC]5[/LOC][VAR]range(0, len(num))[/VAR][VAL]{list(range(0, len(num)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]5[/LOC][VAR]len(num)[/VAR][VAL]{len(num)}[/VAL][/ITE]')
    for i in range(0, len(num)):
        if num[i] in primes:
            total += 1
    return total

hex_key("AB") 
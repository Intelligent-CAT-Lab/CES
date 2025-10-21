from typing import *
def prime_length(string):
    l = len(string)
    if l == 0 or l == 1:
        return False
    print(f'[ITE][LOC]6[/LOC][VAR]range(2, l)[/VAR][VAL]{list(range(2, l))}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR]l[/VAR][VAL]{l}[/VAL][/ITE]')
    for i in range(2, l):
        if l % i == 0:
            return False
    return True

prime_length('Hello') 
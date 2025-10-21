from typing import *
def prime_length(string):
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        print(f'[ITE][LOC]6[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if l % i == 0:
            return False
    return True

prime_length('Hello') 
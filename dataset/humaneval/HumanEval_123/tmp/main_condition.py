from typing import *
def get_odd_collatz(n):
    print(f'[ITE][LOC]2[/LOC][VAR]n%2==0[/VAR][VAL]{n%2==0}[/VAL][/ITE]')
    if n%2==0:
        odd_collatz = [] 
    else:
        odd_collatz = [n]
    while n > 1:
        print(f'[ITE][LOC]7[/LOC][VAR]n % 2 == 0[/VAR][VAL]{n % 2 == 0}[/VAL][/ITE]')
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
            
        print(f'[ITE][LOC]12[/LOC][VAR]n%2 == 1[/VAR][VAL]{n%2 == 1}[/VAL][/ITE]')
        if n%2 == 1:
            odd_collatz.append(int(n))

    return sorted(odd_collatz)

get_odd_collatz(14) 
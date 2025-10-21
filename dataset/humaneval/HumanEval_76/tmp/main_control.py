from typing import *
def is_simple_power(x, n):
    if (n == 1): 
        return (x == 1) 
    power = 1
    print(f'[ITE][LOC]6[/LOC][VAR](power < x)[/VAR][VAL]{(power < x)}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR]power[/VAR][VAL]{power}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR]x[/VAR][VAL]{x}[/VAL][/ITE]')
    while (power < x): 
        power = power * n 
    return (power == x) 

is_simple_power(16, 2)
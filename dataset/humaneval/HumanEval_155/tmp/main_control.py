from typing import *
def even_odd_count(num):
    even_count = 0
    odd_count = 0
    print(f'[ITE][LOC]5[/LOC][VAR]str(abs(num))[/VAR][VAL]{str(abs(num))}[/VAL][/ITE]')
    print(f'[ITE][LOC]5[/LOC][VAR]abs(num)[/VAR][VAL]{abs(num)}[/VAL][/ITE]')
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)

even_odd_count(7) 
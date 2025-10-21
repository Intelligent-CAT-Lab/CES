from typing import *
def digits(n):
    product = 1
    odd_count = 0
    for digit in str(n):
        int_digit = int(digit)
        print(f'[ITE][LOC]6[/LOC][VAR]int_digit%2 == 1[/VAR][VAL]{int_digit%2 == 1}[/VAL][/ITE]')
        if int_digit%2 == 1:
            product= product*int_digit
            odd_count+=1
    print(f'[ITE][LOC]9[/LOC][VAR]odd_count ==0[/VAR][VAL]{odd_count ==0}[/VAL][/ITE]')
    if odd_count ==0:
        return 0
    else:
        return product

digits(5) 
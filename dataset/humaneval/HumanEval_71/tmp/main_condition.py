from typing import *
def triangle_area(a, b, c):
    print(f'[ITE][LOC]2[/LOC][VAR]a + b <= c or a + c <= b or b + c <= a[/VAR][VAL]{a + b <= c or a + c <= b or b + c <= a}[/VAL][/ITE]')
    print(f'[ITE][LOC]2[/LOC][VAR]b + c <= a[/VAR][VAL]{b + c <= a}[/VAL][/ITE]')
    print(f'[ITE][LOC]2[/LOC][VAR]a + b <= c[/VAR][VAL]{a + b <= c}[/VAL][/ITE]')
    print(f'[ITE][LOC]2[/LOC][VAR]a + c <= b[/VAR][VAL]{a + c <= b}[/VAL][/ITE]')
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area

triangle_area(3, 4, 5) 
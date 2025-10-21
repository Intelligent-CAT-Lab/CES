from typing import *
def tri(n):
    print(f'[ITE][LOC]2[/LOC][VAR]n == 0[/VAR][VAL]{n == 0}[/VAL][/ITE]')
    if n == 0:
        return [1]
    my_tri = [1, 3]
    for i in range(2, n + 1):
        print(f'[ITE][LOC]6[/LOC][VAR]i % 2 == 0[/VAR][VAL]{i % 2 == 0}[/VAL][/ITE]')
        if i % 2 == 0:
            my_tri.append(i / 2 + 1)
        else:
            my_tri.append(my_tri[i - 1] + my_tri[i - 2] + (i + 3) / 2)
    return my_tri

tri(3) 
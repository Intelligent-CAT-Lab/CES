from typing import *
def will_it_fly(q,w):
    print(f'[ITE][LOC]2[/LOC][VAR]sum(q) > w[/VAR][VAL]{sum(q) > w}[/VAL][/ITE]')
    if sum(q) > w:
        return False

    i, j = 0, len(q)-1
    while i<j:
        print(f'[ITE][LOC]7[/LOC][VAR]q[i] != q[j][/VAR][VAL]{q[i] != q[j]}[/VAL][/ITE]')
        if q[i] != q[j]:
            return False
        i+=1
        j-=1
    return True

will_it_fly([3, 2, 3], 9)
from typing import *


def tri(n):
    print('[LINE]4[/LINE] may be hit')
    if n == 0:
        print('[LINE]4[/LINE] is hit')
        return [1]
    my_tri = [1, 3]
    for i in range(2, n + 1):
        print('[LINE]8[/LINE] may be hit')
        print('[LINE]10[/LINE] may be hit')
        if i % 2 == 0:
            print('[LINE]8[/LINE] is hit')
            my_tri.append(i / 2 + 1)
        else:
            print('[LINE]10[/LINE] is hit')
            my_tri.append(my_tri[i - 1] + my_tri[i - 2] + (i + 3) / 2)
    return my_tri

tri(20)
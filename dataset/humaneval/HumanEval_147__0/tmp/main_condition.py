from typing import *


def get_max_triples(n):
    A = [i * i - i + 1 for i in range(1, n + 1)]
    ans = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                print(f'[ITE][LOC]9[/LOC][VAR](A[i] + A[j] + A[k]) % 3 == 0[/VAR][VAL]{(A[i] + A[j] + A[k]) % 3 == 0}[/VAL][/ITE]')
                if (A[i] + A[j] + A[k]) % 3 == 0:
                    ans += [(A[i], A[j], A[k])]
    return len(ans)

get_max_triples(100)
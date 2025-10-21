from typing import *


def get_max_triples(n):
    A = [i * i - i + 1 for i in range(1, n + 1)]
    ans = []
    print(f'[ITE][LOC]7[/LOC][VAR]range(n)[/VAR][VAL]{list(range(n))}[/VAL][/ITE]')
    print(f'[ITE][LOC]7[/LOC][VAR]n[/VAR][VAL]{n}[/VAL][/ITE]')
    for i in range(n):
        print(f'[ITE][LOC]8[/LOC][VAR]range((i + 1), n)[/VAR][VAL]{list(range((i + 1), n))}[/VAL][/ITE]')
        print(f'[ITE][LOC]8[/LOC][VAR](i + 1)[/VAR][VAL]{(i + 1)}[/VAL][/ITE]')
        print(f'[ITE][LOC]8[/LOC][VAR]n[/VAR][VAL]{n}[/VAL][/ITE]')
        for j in range(i + 1, n):
            print(f'[ITE][LOC]9[/LOC][VAR]range((j + 1), n)[/VAR][VAL]{list(range((j + 1), n))}[/VAL][/ITE]')
            print(f'[ITE][LOC]9[/LOC][VAR](j + 1)[/VAR][VAL]{(j + 1)}[/VAL][/ITE]')
            print(f'[ITE][LOC]9[/LOC][VAR]n[/VAR][VAL]{n}[/VAL][/ITE]')
            for k in range(j + 1, n):
                if (A[i] + A[j] + A[k]) % 3 == 0:
                    ans += [(A[i], A[j], A[k])]
    return len(ans)

get_max_triples(6)
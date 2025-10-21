from typing import *


def fib4(n: int):
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        print(f'[ITE][LOC]9[/LOC][VAR]_[/VAR][VAL]{_}[/VAL][/ITE]')
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-1]

fib4(12)
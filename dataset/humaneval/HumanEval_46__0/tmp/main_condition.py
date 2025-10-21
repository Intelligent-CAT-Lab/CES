from typing import *


def fib4(n: int):
    results = [0, 0, 2, 0]
    print(f'[ITE][LOC]5[/LOC][VAR]n < 4[/VAR][VAL]{n < 4}[/VAL][/ITE]')
    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-1]

fib4(10)
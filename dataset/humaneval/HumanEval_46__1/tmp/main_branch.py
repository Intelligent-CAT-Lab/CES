from typing import *


def fib4(n: int):
    results = [0, 0, 2, 0]
    print('[LINE]5[/LINE] may be hit')
    if n < 4:
        print('[LINE]5[/LINE] is hit')
        return results[n]

    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-1]

fib4(12)
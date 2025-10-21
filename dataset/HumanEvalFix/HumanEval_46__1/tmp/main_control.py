def fib4(n: int):
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    print(f'[ITE][LOC]6[/LOC][VAR]range(4, (n + 1))[/VAR][VAL]{list(range(4, (n + 1)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR](n + 1)[/VAR][VAL]{(n + 1)}[/VAL][/ITE]')
    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-2]

fib4(12)

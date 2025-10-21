def fib(n: int):
    print(f'[ITE][LOC]1[/LOC][VAR]n == 0[/VAR][VAL]{n == 0}[/VAL][/ITE]')
    if n == 0:
        return 0
    print(f'[ITE][LOC]3[/LOC][VAR]n == 1[/VAR][VAL]{n == 1}[/VAL][/ITE]')
    if n == 1:
        return 1
    print(f'[ITE][LOC]5[/LOC][VAR]n == 2[/VAR][VAL]{n == 2}[/VAL][/ITE]')
    if n == 2:
        return 2
    return fib(n - 1) + fib(n - 2)

fib(12)

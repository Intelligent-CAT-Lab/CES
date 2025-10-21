def is_prime(n):
    if n < 1:
        return False
    print(f'[ITE][LOC]4[/LOC][VAR]range(1, (n - 1))[/VAR][VAL]{list(range(1, (n - 1)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]4[/LOC][VAR](n - 1)[/VAR][VAL]{(n - 1)}[/VAL][/ITE]')
    for k in range(1, n - 1):
        if n % k == 0:
            return False
    return True

is_prime(101)

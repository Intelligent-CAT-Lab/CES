def is_prime(n):
    print(f'[ITE][LOC]1[/LOC][VAR]n < 1[/VAR][VAL]{n < 1}[/VAL][/ITE]')
    if n < 1:
        return False
    for k in range(1, n - 1):
        print(f'[ITE][LOC]4[/LOC][VAR]n % k == 0[/VAR][VAL]{n % k == 0}[/VAL][/ITE]')
        if n % k == 0:
            return False
    return True

is_prime(101)

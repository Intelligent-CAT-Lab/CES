def is_prime(n):
    if n < 1:
        return False
    for k in range(1, n - 1):
        print(f'[ITE][LOC]4[/LOC][VAR]k[/VAR][VAL]{k}[/VAL][/ITE]')
        if n % k == 0:
            return False
    return True

is_prime(101)

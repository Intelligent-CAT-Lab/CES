def prime_fib(n: int):
    import math

    def is_prime(p):
        if p < 2:
            return False
        print(f'[ITE][LOC]7[/LOC][VAR]range(2, min(int(math.sqrt(p)), p))[/VAR][VAL]{list(range(2, min(int(math.sqrt(p)), p)))}[/VAL][/ITE]')
        print(f'[ITE][LOC]7[/LOC][VAR]min(int(math.sqrt(p)), p)[/VAR][VAL]{min(int(math.sqrt(p)), p)}[/VAL][/ITE]')
        for k in range(2, min(int(math.sqrt(p)), p)):
            if p % k == 0:
                return False
        return True
    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]

prime_fib(4)

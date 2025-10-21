def count_up_to(n):
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            print(f'[ITE][LOC]5[/LOC][VAR]j % i == 0[/VAR][VAL]{j % i == 0}[/VAL][/ITE]')
            if j % i == 0:
                is_prime = False
                break
        print(f'[ITE][LOC]8[/LOC][VAR]is_prime[/VAR][VAL]{is_prime}[/VAL][/ITE]')
        if is_prime:
            primes.append(i)
    return primes


count_up_to(5)

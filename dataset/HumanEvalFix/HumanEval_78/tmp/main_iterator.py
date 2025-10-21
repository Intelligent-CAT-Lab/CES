def hex_key(num):
    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 1
    for i in range(0, len(num)):
        print(f'[ITE][LOC]4[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if num[i] in primes:
            total += 1
    return total

hex_key('AB')

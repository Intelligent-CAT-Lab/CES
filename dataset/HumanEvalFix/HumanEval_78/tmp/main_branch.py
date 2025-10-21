def hex_key(num):
    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 1
    for i in range(0, len(num)):
        print('[LINE]4[/LINE] may be hit')
        if num[i] in primes:
            print('[LINE]4[/LINE] is hit')
            total += 1
    return total

hex_key('AB')
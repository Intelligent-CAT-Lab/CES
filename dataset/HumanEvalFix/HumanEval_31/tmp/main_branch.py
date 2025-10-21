def is_prime(n):
    print('[LINE]1[/LINE] may be hit')
    if n < 1:
        print('[LINE]1[/LINE] is hit')
        return False
    for k in range(1, n - 1):
        print('[LINE]4[/LINE] may be hit')
        if n % k == 0:
            print('[LINE]4[/LINE] is hit')
            return False
    return True

is_prime(101)
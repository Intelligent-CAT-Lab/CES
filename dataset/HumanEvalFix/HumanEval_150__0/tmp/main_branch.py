def x_or_y(n, x, y):
    print('[LINE]1[/LINE] may be hit')
    if n == 1:
        print('[LINE]1[/LINE] is hit')
        return y
    for i in range(2, n):
        print('[LINE]4[/LINE] may be hit')
        if n % i - 1 == 0:
            print('[LINE]4[/LINE] is hit')
            return y
            break
    else:
        return x

x_or_y(3, 33, 5212)
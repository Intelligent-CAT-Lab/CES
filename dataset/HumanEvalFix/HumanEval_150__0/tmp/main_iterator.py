def x_or_y(n, x, y):
    if n == 1:
        return y
    for i in range(2, n):
        print(f'[ITE][LOC]4[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if n % i - 1 == 0:
            return y
            break
    else:
        return x

x_or_y(3, 33, 5212)

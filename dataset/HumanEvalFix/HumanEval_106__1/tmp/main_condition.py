def f(n):
    ret = []
    for i in range(1,n+1):
        print(f'[ITE][LOC]3[/LOC][VAR]i%2 == 0[/VAR][VAL]{i%2 == 0}[/VAL][/ITE]')
        if i%2 == 0:
            x = 1
            for j in range(1,i+1): x *= i
            ret += [x]
        else:
            x = 0
            for j in range(1,i+1): x += j
            ret += [x]
    return ret

f(7)

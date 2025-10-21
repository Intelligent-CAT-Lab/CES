def f(n):
    ret = []
    for i in range(1,n+1):
        print(f'[ITE][LOC]3[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if i%2 == 0:
            x = 1
            for j in range(1,i+1): x *= i
            print(f'[ITE][LOC]6[/LOC][VAR]j[/VAR][VAL]{j}[/VAL][/ITE]')
            ret += [x]
        else:
            x = 0
            for j in range(1,i+1): x += j
            print(f'[ITE][LOC]10[/LOC][VAR]j[/VAR][VAL]{j}[/VAL][/ITE]')
            ret += [x]
    return ret

f(7)

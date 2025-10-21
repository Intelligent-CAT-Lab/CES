def fruit_distribution(s,n):
    lis = list()
    for i in s.split(' '):
        print(f'[ITE][LOC]3[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis) - 1

fruit_distribution('5 apples and 6 oranges', 21)

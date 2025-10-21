def fruit_distribution(s,n):
    lis = list()
    print(f"[ITE][LOC]3[/LOC][VAR]s.split(' ')[/VAR][VAL]{s.split(' ')}[/VAL][/ITE]")
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis) - 1

fruit_distribution('5 apples and 6 oranges', 21)

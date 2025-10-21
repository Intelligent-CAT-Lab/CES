def tri(n):
    if n == 0:
        return [1]
    my_tri = [1, 3]
    print(f'[ITE][LOC]5[/LOC][VAR]range(2, (n + 1))[/VAR][VAL]{list(range(2, (n + 1)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]5[/LOC][VAR](n + 1)[/VAR][VAL]{(n + 1)}[/VAL][/ITE]')
    for i in range(2, n + 1):
        if i % 2 == 0:
            my_tri.append(i / 2 + 1)
        else:
            my_tri.append(my_tri[i - 1] + my_tri[i - 2] + i + (i + 3) / 2)
    return my_tri

tri(20)

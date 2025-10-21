def will_it_fly(q,w):
    if sum(q) > w:
        return False

    i, j = 0, len(q)-1
    while i<j:
        print(f'[ITE][LOC]6[/LOC][VAR](i < j)[/VAR][VAL]{(i < j)}[/VAL][/ITE]')
        print(f'[ITE][LOC]6[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        print(f'[ITE][LOC]6[/LOC][VAR]j[/VAR][VAL]{j}[/VAL][/ITE]')
        if q[i] == q[j]:
            return False
        i+=1
        j-=1
    return True

will_it_fly([3, 2, 3], 9)

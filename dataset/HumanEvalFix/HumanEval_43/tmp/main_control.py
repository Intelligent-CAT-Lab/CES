def pairs_sum_to_zero(l):
    print(f'[ITE][LOC]2[/LOC][VAR]enumerate(l)[/VAR][VAL]{list(enumerate(l))}[/VAL][/ITE]')
    print(f'[ITE][LOC]2[/LOC][VAR]l[/VAR][VAL]{l}[/VAL][/ITE]')
    for i, l1 in enumerate(l):
        print(f'[ITE][LOC]3[/LOC][VAR]range(i, len(l))[/VAR][VAL]{list(range(i, len(l)))}[/VAL][/ITE]')
        print(f'[ITE][LOC]3[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        print(f'[ITE][LOC]3[/LOC][VAR]len(l)[/VAR][VAL]{len(l)}[/VAL][/ITE]')
        for j in range(i, len(l)):
            if l1 + l[j] == 0:
                return True
    return False

pairs_sum_to_zero([1, 3, 5, 0])

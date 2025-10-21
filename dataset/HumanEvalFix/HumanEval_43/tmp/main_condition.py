def pairs_sum_to_zero(l):
    for i, l1 in enumerate(l):
        for j in range(i, len(l)):
            print(f'[ITE][LOC]3[/LOC][VAR]l1 + l[j] == 0[/VAR][VAL]{l1 + l[j] == 0}[/VAL][/ITE]')
            if l1 + l[j] == 0:
                return True
    return False

pairs_sum_to_zero([1, 3, 5, 0])

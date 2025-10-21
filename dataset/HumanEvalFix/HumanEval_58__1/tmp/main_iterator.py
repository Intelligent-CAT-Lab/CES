def common(l1: list, l2: list):
    ret = set()
    for e1 in l1:
        print(f'[ITE][LOC]3[/LOC][VAR]e1[/VAR][VAL]{e1}[/VAL][/ITE]')
        for e2 in l2:
            print(f'[ITE][LOC]4[/LOC][VAR]e2[/VAR][VAL]{e2}[/VAL][/ITE]')
            ret.add(e1)
    return sorted(list(ret))

common([5, 3, 2, 8], [3, 2])

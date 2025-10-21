def cycpattern_check(a , b):
    l = len(b)
    pat = b + b
    print(f'[ITE][LOC]4[/LOC][VAR]range(((len(a) - l) + 1))[/VAR][VAL]{list(range(((len(a) - l) + 1)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]4[/LOC][VAR]((len(a) - l) + 1)[/VAR][VAL]{((len(a) - l) + 1)}[/VAL][/ITE]')
    for i in range(len(a) - l + 1):
        print(f'[ITE][LOC]5[/LOC][VAR]range(((len(b) - l) + 1))[/VAR][VAL]{list(range(((len(b) - l) + 1)))}[/VAL][/ITE]')
        print(f'[ITE][LOC]5[/LOC][VAR]((len(b) - l) + 1)[/VAR][VAL]{((len(b) - l) + 1)}[/VAL][/ITE]')
        for j in range(len(b) - l + 1):
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False

cycpattern_check('efef', 'fee')

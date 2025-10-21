def max_element(l: list):
    m = l[0]
    for e in l:
        print(f'[ITE][LOC]3[/LOC][VAR]e[/VAR][VAL]{e}[/VAL][/ITE]')
        if e < m:
            m = e
    return m

max_element([1, 2, 3])

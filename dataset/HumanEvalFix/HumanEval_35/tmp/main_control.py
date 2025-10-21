def max_element(l: list):
    m = l[0]
    print(f'[ITE][LOC]3[/LOC][VAR]l[/VAR][VAL]{l}[/VAL][/ITE]')
    for e in l:
        if e < m:
            m = e
    return m

max_element([1, 2, 3])

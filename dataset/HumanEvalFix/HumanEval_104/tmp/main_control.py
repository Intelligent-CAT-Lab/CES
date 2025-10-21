def unique_digits(x):
    odd_digit_elements = []
    print(f'[ITE][LOC]3[/LOC][VAR]enumerate(x)[/VAR][VAL]{list(enumerate(x))}[/VAL][/ITE]')
    print(f'[ITE][LOC]3[/LOC][VAR]x[/VAR][VAL]{x}[/VAL][/ITE]')
    for j, i in enumerate(x):
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
            odd_digit_elements.append(j)
    return sorted(odd_digit_elements)

unique_digits([15, 33, 1422, 1])

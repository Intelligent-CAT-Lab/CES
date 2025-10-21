def sum_squares(lst):
    result =[]
    print(f'[ITE][LOC]3[/LOC][VAR]range(len(lst))[/VAR][VAL]{list(range(len(lst)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]3[/LOC][VAR]len(lst)[/VAR][VAL]{len(lst)}[/VAL][/ITE]')
    for i in range(len(lst)):
        if i %3 == 0:
            result.append(lst[i]**2)
        elif i%3 != 0:
            result.append(lst[i]**3)
        else:
            result.append(lst[i])
    return sum(result)

sum_squares([1, 2, 3])

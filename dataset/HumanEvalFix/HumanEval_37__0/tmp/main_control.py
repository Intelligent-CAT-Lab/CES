def sort_even(l: list):
    evens = l[::2]
    odds = l[1::2]
    odds.sort()
    ans = []
    print(f'[ITE][LOC]6[/LOC][VAR]zip(evens, odds)[/VAR][VAL]{list(zip(evens, odds))}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR]evens[/VAR][VAL]{evens}[/VAL][/ITE]')
    print(f'[ITE][LOC]6[/LOC][VAR]odds[/VAR][VAL]{odds}[/VAL][/ITE]')
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans

tuple(sort_even([5, 3, (- 5), 2, (- 3), 3, 9, 0, 123, 1, (- 10)]))

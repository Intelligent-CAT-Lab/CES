def sum_squares(lst):
    import math
    squared = 0
    print(f'[ITE][LOC]4[/LOC][VAR]lst[/VAR][VAL]{lst}[/VAL][/ITE]')
    for i in lst:
        squared += math.ceil(i)*2
    return squared

sum_squares([1, 3, 5, 7])

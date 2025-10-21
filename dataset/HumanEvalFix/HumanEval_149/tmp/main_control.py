def sorted_list_sum(lst):
    lst.sort()
    new_lst = []
    print(f'[ITE][LOC]4[/LOC][VAR]lst[/VAR][VAL]{lst}[/VAL][/ITE]')
    for i in lst:
        if len(i)%2 == 0:
            new_lst.append(i)
    return new_lst

sorted_list_sum(['aaaa', 'bbbb', 'dd', 'cc'])

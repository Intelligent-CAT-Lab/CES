def sorted_list_sum(lst):
    lst.sort()
    new_lst = []
    for i in lst:
        print(f'[ITE][LOC]4[/LOC][VAR]len(i)%2 == 0[/VAR][VAL]{len(i)%2 == 0}[/VAL][/ITE]')
        if len(i)%2 == 0:
            new_lst.append(i)
    return new_lst

sorted_list_sum(['aaaa', 'bbbb', 'dd', 'cc'])

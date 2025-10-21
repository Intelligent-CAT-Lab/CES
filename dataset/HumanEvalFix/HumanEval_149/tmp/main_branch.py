def sorted_list_sum(lst):
    lst.sort()
    new_lst = []
    for i in lst:
        print('[LINE]4[/LINE] may be hit')
        if len(i)%2 == 0:
            print('[LINE]4[/LINE] is hit')
            new_lst.append(i)
    return new_lst

sorted_list_sum(['aaaa', 'bbbb', 'dd', 'cc'])
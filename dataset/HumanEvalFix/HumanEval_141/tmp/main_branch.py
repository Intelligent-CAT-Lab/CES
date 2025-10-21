def file_name_check(file_name):
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    print('[LINE]3[/LINE] may be hit')
    if len(lst) != 2:
        print('[LINE]3[/LINE] is hit')
        return 'No'
    print('[LINE]5[/LINE] may be hit')
    if len(lst[0]) == 0:
        print('[LINE]5[/LINE] is hit')
        return 'No'
    print('[LINE]7[/LINE] may be hit')
    if not lst[0][0].isalpha():
        print('[LINE]7[/LINE] is hit')
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    print('[LINE]10[/LINE] may be hit')
    if t > 3:
        print('[LINE]10[/LINE] is hit')
        return 'No'
    return 'Yes'

file_name_check('s1sdf3.asd')
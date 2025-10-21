def choose_num(x, y):
    print('[LINE]1[/LINE] may be hit')
    if x > y:
        print('[LINE]1[/LINE] is hit')
        return -1
    print('[LINE]3[/LINE] may be hit')
    if y % 2 == 0:
        print('[LINE]3[/LINE] is hit')
        return y
    print('[LINE]5[/LINE] may be hit')
    if x == y:
        print('[LINE]5[/LINE] is hit')
        return -1
    return x - 1

choose_num(12, 15)
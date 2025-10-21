def fibfib(n: int):
    print('[LINE]1[/LINE] may be hit')
    if n == 0:
        print('[LINE]1[/LINE] is hit')
        return 0
    print('[LINE]3[/LINE] may be hit')
    if n == 1:
        print('[LINE]3[/LINE] is hit')
        return 1
    print('[LINE]5[/LINE] may be hit')
    if n == 2:
        print('[LINE]5[/LINE] is hit')
        return 2
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)

fibfib(10)
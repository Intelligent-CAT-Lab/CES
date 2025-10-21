def starts_one_ends(n):
    print('[LINE]1[/LINE] may be hit')
    if n == 1: 
        print('[LINE]1[/LINE] is hit')
        return 1
        
    return 18 * n * (10 ** (n - 2))

starts_one_ends(2)
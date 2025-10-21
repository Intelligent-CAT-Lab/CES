def fruit_distribution(s,n):
    lis = list()
    for i in s.split(' '):
        print('[LINE]3[/LINE] may be hit')
        if i.isdigit():
            print('[LINE]3[/LINE] is hit')
            lis.append(int(i))
    return n - sum(lis) - 1

fruit_distribution('5 apples and 6 oranges', 21)
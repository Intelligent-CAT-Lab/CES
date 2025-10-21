def f(n):
    ret = []
    for i in range(1,n+1):
        print('[LINE]3[/LINE] may be hit')
        print('[LINE]7[/LINE] may be hit')
        if i%2 == 0:
            print('[LINE]3[/LINE] is hit')
            x = 1
            for j in range(1,i+1): x *= i
            ret += [x]
        else:
            print('[LINE]7[/LINE] is hit')
            x = 0
            for j in range(1,i+1): x += j
            ret += [x]
    return ret

f(7)
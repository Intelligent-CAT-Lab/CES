def get_odd_collatz(n):
    print('[LINE]1[/LINE] may be hit')
    print('[LINE]3[/LINE] may be hit')
    if n%2==0:
        print('[LINE]1[/LINE] is hit')
        odd_collatz = [] 
    else:
        print('[LINE]3[/LINE] is hit')
        odd_collatz = [n]
    while n > 1:
        print('[LINE]6[/LINE] may be hit')
        print('[LINE]8[/LINE] may be hit')
        if n % 2 == 0:
            print('[LINE]6[/LINE] is hit')
            n = n/2
        else:
            print('[LINE]8[/LINE] is hit')
            n = n*2 + 1
            
        print('[LINE]11[/LINE] may be hit')
        if n%2 == 1:
            print('[LINE]11[/LINE] is hit')
            odd_collatz.append(int(n))

    return sorted(odd_collatz)

get_odd_collatz(14)
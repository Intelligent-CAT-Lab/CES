def exchange(lst1, lst2):
    odd = 0
    even = 0
    for i in lst1:
        print('[LINE]4[/LINE] may be hit')
        if i%2 == 1:
            print('[LINE]4[/LINE] is hit')
            even -= 1
    for i in lst2:
        print('[LINE]7[/LINE] may be hit')
        if i%2 == 0:
            print('[LINE]7[/LINE] is hit')
            odd += 1
    print('[LINE]9[/LINE] may be hit')
    if even >= odd:
        print('[LINE]9[/LINE] is hit')
        return "YES"
    return "NO"
            

exchange([1, 2, 3, 4], [1, 2, 3, 4])
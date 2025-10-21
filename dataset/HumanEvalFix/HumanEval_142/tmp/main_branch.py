def sum_squares(lst):
    result =[]
    for i in range(len(lst)):
        print('[LINE]3[/LINE] may be hit')
        print('[LINE]5[/LINE] may be hit')
        print('[LINE]7[/LINE] may be hit')
        if i %3 == 0:
            print('[LINE]3[/LINE] is hit')
            result.append(lst[i]**2)
        elif i%3 != 0:
            print('[LINE]5[/LINE] is hit')
            result.append(lst[i]**3)
        else:
            print('[LINE]7[/LINE] is hit')
            result.append(lst[i])
    return sum(result)

sum_squares([1, 2, 3])
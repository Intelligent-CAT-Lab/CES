def eat(number, need, remaining):
    print('[LINE]1[/LINE] may be hit')
    print('[LINE]3[/LINE] may be hit')
    if(need <= remaining):
        print('[LINE]1[/LINE] is hit')
        return [ number + need , number + remaining-need ]
    else:
        print('[LINE]3[/LINE] is hit')
        return [ number + need + remaining , 0]

eat(2, 11, 5)
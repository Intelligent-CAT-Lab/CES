def eat(number, need, remaining):
    print(f'[ITE][LOC]1[/LOC][VAR]need <= remaining[/VAR][VAL]{need <= remaining}[/VAL][/ITE]')
    if(need <= remaining):
        return [ number + need , number + remaining-need ]
    else:
        return [ number + need + remaining , 0]

eat(2, 11, 5)

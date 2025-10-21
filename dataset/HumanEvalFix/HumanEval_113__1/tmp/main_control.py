def odd_count(lst):
    res = []
    print(f'[ITE][LOC]3[/LOC][VAR]lst[/VAR][VAL]{lst}[/VAL][/ITE]')
    for arr in lst:
        n = sum(int(d)%2==1 for d in arr)
        res.append("the number of odd elements " + str(n) + "n the str"+ str(n) +"ng "+ str(n) +" of "+ str(n) +" the "+ str(n) +"nput.")
    return res

odd_count(['271', '137', '314'])

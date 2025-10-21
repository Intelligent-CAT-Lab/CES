def histogram(test):
    dict1={}
    list1=test.split(" ")
    t=1

    for i in list1:
        print(f"[ITE][LOC]6[/LOC][VAR](list1.count(i)>t) and i!=''[/VAR][VAL]{(list1.count(i)>t) and i!=''}[/VAL][/ITE]")
        print(f"[ITE][LOC]6[/LOC][VAR]i!=''[/VAR][VAL]{i!=''}[/VAL][/ITE]")
        print(f'[ITE][LOC]6[/LOC][VAR]list1.count(i)>t[/VAR][VAL]{list1.count(i)>t}[/VAL][/ITE]')
        if(list1.count(i)>t) and i!='':
            t=list1.count(i)
    print(f'[ITE][LOC]8[/LOC][VAR]t>0[/VAR][VAL]{t>0}[/VAL][/ITE]')
    if t>0:
        for i in list1:
            print(f'[ITE][LOC]10[/LOC][VAR]list1.count(i)==t[/VAR][VAL]{list1.count(i)==t}[/VAL][/ITE]')
            if(list1.count(i)==t):
                
                dict1[i]=t
    return dict1

histogram('')

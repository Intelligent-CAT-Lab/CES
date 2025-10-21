def histogram(test):
    dict1={}
    list1=test.split(" ")
    t=1

    print(f'[ITE][LOC]6[/LOC][VAR]list1[/VAR][VAL]{list1}[/VAL][/ITE]')
    for i in list1:
        if(list1.count(i)>t) and i!='':
            t=list1.count(i)
    if t>0:
        print(f'[ITE][LOC]10[/LOC][VAR]list1[/VAR][VAL]{list1}[/VAL][/ITE]')
        for i in list1:
            if(list1.count(i)==t):
                
                dict1[i]=t
    return dict1

histogram('')

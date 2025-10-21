def histogram(test):
    dict1={}
    list1=test.split(" ")
    t=1

    for i in list1:
        print('[LINE]6[/LINE] may be hit')
        if(list1.count(i)>t) and i!='':
            print('[LINE]6[/LINE] is hit')
            t=list1.count(i)
    print('[LINE]8[/LINE] may be hit')
    if t>0:
        print('[LINE]8[/LINE] is hit')
        for i in list1:
            print('[LINE]10[/LINE] may be hit')
            if(list1.count(i)==t):
                print('[LINE]10[/LINE] is hit')
                
                dict1[i]=t
    return dict1

histogram('')
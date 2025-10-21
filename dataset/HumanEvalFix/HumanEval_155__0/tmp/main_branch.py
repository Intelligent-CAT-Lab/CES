def even_odd_count(num):
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        print('[LINE]4[/LINE] may be hit')
        if int(i)%2==0:
            print('[LINE]4[/LINE] is hit')
            even_count +=1
    return (even_count, odd_count)

even_odd_count((- 345821))
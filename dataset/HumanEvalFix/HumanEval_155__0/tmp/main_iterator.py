def even_odd_count(num):
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        print(f'[ITE][LOC]4[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if int(i)%2==0:
            even_count +=1
    return (even_count, odd_count)

even_odd_count((- 345821))

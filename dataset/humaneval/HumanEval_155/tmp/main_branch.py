from typing import *
def even_odd_count(num):
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        print('[LINE]5[/LINE] may be hit')
        print('[LINE]7[/LINE] may be hit')
        if int(i)%2==0:
            print('[LINE]5[/LINE] is hit')
            even_count +=1
        else:
            print('[LINE]7[/LINE] is hit')
            odd_count +=1
    return (even_count, odd_count)

even_odd_count(7) 
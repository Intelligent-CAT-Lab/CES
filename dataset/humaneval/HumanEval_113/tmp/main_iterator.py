from typing import *
def odd_count(lst):
    res = []
    for arr in lst:
        print(f'[ITE][LOC]4[/LOC][VAR]arr[/VAR][VAL]{arr}[/VAL][/ITE]')
        n = sum(int(d)%2==1 for d in arr)
        res.append("the number of odd elements " + str(n) + "n the str"+ str(n) +"ng "+ str(n) +" of the "+ str(n) +"nput.")
    return res

odd_count(['1234567']) 
from typing import *
def skjkasdkd(lst):
    def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            print('[LINE]4[/LINE] may be hit')
            if n%i==0:
                print('[LINE]4[/LINE] is hit')
                return False

        return True
    maxx = 0
    i = 0
    while i < len(lst):
        print('[LINE]11[/LINE] may be hit')
        if(lst[i] > maxx and isPrime(lst[i])):
            print('[LINE]11[/LINE] is hit')
            maxx = lst[i]
        i+=1
    result = sum(int(digit) for digit in str(maxx))
    return result


skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]) 
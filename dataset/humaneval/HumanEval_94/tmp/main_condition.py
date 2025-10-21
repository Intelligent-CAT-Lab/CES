from typing import *
def skjkasdkd(lst):
    def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            print(f'[ITE][LOC]4[/LOC][VAR]n%i==0[/VAR][VAL]{n%i==0}[/VAL][/ITE]')
            if n%i==0:
                return False

        return True
    maxx = 0
    i = 0
    while i < len(lst):
        print(f'[ITE][LOC]11[/LOC][VAR](lst[i] > maxx and isPrime(lst[i]))[/VAR][VAL]{(lst[i] > maxx and isPrime(lst[i]))}[/VAL][/ITE]')
        print(f'[ITE][LOC]11[/LOC][VAR]lst[i] > maxx[/VAR][VAL]{lst[i] > maxx}[/VAL][/ITE]')
        print(f'[ITE][LOC]11[/LOC][VAR]isPrime(lst[i])[/VAR][VAL]{isPrime(lst[i])}[/VAL][/ITE]')
        if(lst[i] > maxx and isPrime(lst[i])):
            maxx = lst[i]
        i+=1
    result = sum(int(digit) for digit in str(maxx))
    return result


skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]) 
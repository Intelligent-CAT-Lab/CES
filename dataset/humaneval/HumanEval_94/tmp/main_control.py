from typing import *
def skjkasdkd(lst):
    def isPrime(n):
        print(f'[ITE][LOC]4[/LOC][VAR]range(2, (int((n ** 0.5)) + 1))[/VAR][VAL]{list(range(2, (int((n ** 0.5)) + 1)))}[/VAL][/ITE]')
        print(f'[ITE][LOC]4[/LOC][VAR](int((n ** 0.5)) + 1)[/VAR][VAL]{(int((n ** 0.5)) + 1)}[/VAL][/ITE]')
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False

        return True
    maxx = 0
    i = 0
    print(f'[ITE][LOC]11[/LOC][VAR](i < len(lst))[/VAR][VAL]{(i < len(lst))}[/VAL][/ITE]')
    print(f'[ITE][LOC]11[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
    print(f'[ITE][LOC]11[/LOC][VAR]len(lst)[/VAR][VAL]{len(lst)}[/VAL][/ITE]')
    while i < len(lst):
        if(lst[i] > maxx and isPrime(lst[i])):
            maxx = lst[i]
        i+=1
    result = sum(int(digit) for digit in str(maxx))
    return result


skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]) 
from typing import *


def skjkasdkd(lst):
    def isPrime(n):
        for i in range(2, int(n**0.5) + 1):
            print(f'[ITE][LOC]6[/LOC][VAR]n % i == 0[/VAR][VAL]{n % i == 0}[/VAL][/ITE]')
            if n % i == 0:
                return False

        return True
    maxx = 0
    i = 0
    while i < len(lst):
        print(f'[ITE][LOC]13[/LOC][VAR](lst[i] > maxx and isPrime(lst[i]))[/VAR][VAL]{(lst[i] > maxx and isPrime(lst[i]))}[/VAL][/ITE]')
        print(f'[ITE][LOC]13[/LOC][VAR]lst[i] > maxx[/VAR][VAL]{lst[i] > maxx}[/VAL][/ITE]')
        print(f'[ITE][LOC]13[/LOC][VAR]isPrime(lst[i])[/VAR][VAL]{isPrime(lst[i])}[/VAL][/ITE]')
        if (lst[i] > maxx and isPrime(lst[i])):
            maxx = lst[i]
        i += 1
    result = sum(int(digit) for digit in str(maxx))
    return result

skjkasdkd([127, 97, 8192])
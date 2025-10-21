from typing import *


def skjkasdkd(lst):
    def isPrime(n):
        for i in range(2, int(n**0.5) + 1):
            print('[LINE]6[/LINE] may be hit')
            if n % i == 0:
                print('[LINE]6[/LINE] is hit')
                return False

        return True
    maxx = 0
    i = 0
    while i < len(lst):
        print('[LINE]13[/LINE] may be hit')
        if (lst[i] > maxx and isPrime(lst[i])):
            print('[LINE]13[/LINE] is hit')
            maxx = lst[i]
        i += 1
    result = sum(int(digit) for digit in str(maxx))
    return result

skjkasdkd([0,8,1,2,1,7])
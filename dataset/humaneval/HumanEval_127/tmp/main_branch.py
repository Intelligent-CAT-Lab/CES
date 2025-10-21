from typing import *
def intersection(interval1, interval2):
    def is_prime(num):
        print('[LINE]3[/LINE] may be hit')
        if num == 1 or num == 0:
            print('[LINE]3[/LINE] is hit')
            return False
        print('[LINE]5[/LINE] may be hit')
        if num == 2:
            print('[LINE]5[/LINE] is hit')
            return True
        for i in range(2, num):
            print('[LINE]8[/LINE] may be hit')
            if num%i == 0:
                print('[LINE]8[/LINE] is hit')
                return False
        return True

    l = max(interval1[0], interval2[0])
    r = min(interval1[1], interval2[1])
    length = r - l
    print('[LINE]15[/LINE] may be hit')
    if length > 0 and is_prime(length):
        print('[LINE]15[/LINE] is hit')
        return "YES"
    return "NO"

intersection((1, 2), (2, 3)) 
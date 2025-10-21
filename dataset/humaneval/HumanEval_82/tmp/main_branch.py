from typing import *
def prime_length(string):
    l = len(string)
    print('[LINE]3[/LINE] may be hit')
    if l == 0 or l == 1:
        print('[LINE]3[/LINE] is hit')
        return False
    for i in range(2, l):
        print('[LINE]6[/LINE] may be hit')
        if l % i == 0:
            print('[LINE]6[/LINE] is hit')
            return False
    return True

prime_length('Hello') 
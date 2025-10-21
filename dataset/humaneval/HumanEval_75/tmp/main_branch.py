from typing import *
def is_multiply_prime(a):
    def is_prime(n):
        for j in range(2,n):
            print('[LINE]4[/LINE] may be hit')
            if n%j == 0:
                print('[LINE]4[/LINE] is hit')
                return False
        return True

    for i in range(2,101):
        print('[LINE]9[/LINE] may be hit')
        if not is_prime(i): continue
            print('[LINE]9[/LINE] is hit')
        for j in range(2,101):
            print('[LINE]11[/LINE] may be hit')
            if not is_prime(j): continue
                print('[LINE]11[/LINE] is hit')
            for k in range(2,101):
                print('[LINE]13[/LINE] may be hit')
                if not is_prime(k): continue
                    print('[LINE]13[/LINE] is hit')
                print('[LINE]14[/LINE] may be hit')
                if i*j*k == a: return True
                    print('[LINE]14[/LINE] is hit')
    return False

is_multiply_prime(5) 
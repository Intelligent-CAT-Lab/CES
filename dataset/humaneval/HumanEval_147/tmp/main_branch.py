from typing import *
def get_max_triples(n):
    A = [i*i - i + 1 for i in range(1,n+1)]
    ans = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                print('[LINE]7[/LINE] may be hit')
                if (A[i]+A[j]+A[k])%3 == 0:
                    print('[LINE]7[/LINE] is hit')
                    ans += [(A[i],A[j],A[k])]
    return len(ans)

get_max_triples(5) 
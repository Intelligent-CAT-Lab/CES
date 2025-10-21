def get_max_triples(n):
    A = [i*i for i in range(1,n+1)]
    ans = []
    for i in range(n):
        print(f'[ITE][LOC]4[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        for j in range(i+1,n):
            print(f'[ITE][LOC]5[/LOC][VAR]j[/VAR][VAL]{j}[/VAL][/ITE]')
            for k in range(j+1,n):
                print(f'[ITE][LOC]6[/LOC][VAR]k[/VAR][VAL]{k}[/VAL][/ITE]')
                if (A[i]+A[j]+A[k])%3 == 0:
                    ans += [(A[i],A[j],A[k])]
    return len(ans)

get_max_triples(5)

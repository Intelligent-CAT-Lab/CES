def search(lst):
    frq = [0] * (max(lst) + 1)
    for i in lst:
        print(f'[ITE][LOC]3[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        frq[i] += 1;

    ans = 0
    for i in range(1, len(frq)):
        print(f'[ITE][LOC]7[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if frq[i] >= i:
            ans = i
    
    return ans

search([3, 3])

def search(lst):
    frq = [0] * (max(lst) + 1)
    print(f'[ITE][LOC]3[/LOC][VAR]lst[/VAR][VAL]{lst}[/VAL][/ITE]')
    for i in lst:
        frq[i] += 1;

    ans = 0
    print(f'[ITE][LOC]7[/LOC][VAR]range(1, len(frq))[/VAR][VAL]{list(range(1, len(frq)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]7[/LOC][VAR]len(frq)[/VAR][VAL]{len(frq)}[/VAL][/ITE]')
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    
    return ans

search([3, 3])

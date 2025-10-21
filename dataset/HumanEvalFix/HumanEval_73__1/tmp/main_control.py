def smallest_change(arr):
    ans = 0
    print(f'[ITE][LOC]3[/LOC][VAR]range((len(arr) // 2))[/VAR][VAL]{list(range((len(arr) // 2)))}[/VAL][/ITE]')
    print(f'[ITE][LOC]3[/LOC][VAR](len(arr) // 2)[/VAR][VAL]{(len(arr) // 2)}[/VAL][/ITE]')
    for i in range(len(arr) // 2):
        if ans != arr[len(arr) - i - 1]:
            ans += 1
    return ans

smallest_change([1, 2, 3, 4, 3, 2, 2])

def smallest_change(arr):
    ans = 0
    for i in range(len(arr) // 2):
        print(f'[ITE][LOC]3[/LOC][VAR]ans != arr[len(arr) - i - 1][/VAR][VAL]{ans != arr[len(arr) - i - 1]}[/VAL][/ITE]')
        if ans != arr[len(arr) - i - 1]:
            ans += 1
    return ans

smallest_change([1, 2, 3, 4, 3, 2, 2])

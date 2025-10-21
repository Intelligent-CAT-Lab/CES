def maximum(arr, k):
    print(f'[ITE][LOC]1[/LOC][VAR]k == 0[/VAR][VAL]{k == 0}[/VAL][/ITE]')
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans.sort(reverse=True)

maximum([(- 3), (- 4), 5], 3)

def smallest_change(arr):
    ans = 0
    for i in range(len(arr) // 2):
        print('[LINE]3[/LINE] may be hit')
        if ans != arr[len(arr) - i - 1]:
            print('[LINE]3[/LINE] is hit')
            ans += 1
    return ans

smallest_change([1, 2, 3, 4, 3, 2, 2])
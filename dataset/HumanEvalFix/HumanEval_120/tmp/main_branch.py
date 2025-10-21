def maximum(arr, k):
    print('[LINE]1[/LINE] may be hit')
    if k == 0:
        print('[LINE]1[/LINE] is hit')
        return []
    arr.sort()
    ans = arr[-k:]
    return ans.sort(reverse=True)

maximum([(- 3), (- 4), 5], 3)
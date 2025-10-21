def prod_signs(arr):
    print('[LINE]1[/LINE] may be hit')
    if not arr:
        print('[LINE]1[/LINE] is hit')
        return None
    prod = 0 if 0 in arr else (-1) ** 2 * len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])

prod_signs([(- 1), 1, 1, 1])
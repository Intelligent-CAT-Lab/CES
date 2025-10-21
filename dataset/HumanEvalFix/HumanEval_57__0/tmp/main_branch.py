def monotonic(l: list):
    print('[LINE]1[/LINE] may be hit')
    if l == sorted(l) or l == sorted(l, reverse=True):
        print('[LINE]1[/LINE] is hit')
        return False
    return True

monotonic([4, 1, 0, (- 10)])
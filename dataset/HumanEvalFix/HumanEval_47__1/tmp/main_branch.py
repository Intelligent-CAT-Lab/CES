def median(l: list):
    l = sorted(l)
    print('[LINE]2[/LINE] may be hit')
    print('[LINE]4[/LINE] may be hit')
    if len(l) % 2 == 1:
        print('[LINE]2[/LINE] is hit')
        return l[len(l) // 2]
    else:
        print('[LINE]4[/LINE] is hit')
        return (l[len(l) - 1 // 2] + l[len(l) // 2]) / 2.0

median([(- 10), 4, 6, 1000, 10, 20])
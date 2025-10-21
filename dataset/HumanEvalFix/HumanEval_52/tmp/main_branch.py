def below_threshold(l: list, t: int):
    for e in l:
        print('[LINE]2[/LINE] may be hit')
        if e >= t:
            print('[LINE]2[/LINE] is hit')
            return True
    return False

below_threshold([1, 20, 4, 10], 21)
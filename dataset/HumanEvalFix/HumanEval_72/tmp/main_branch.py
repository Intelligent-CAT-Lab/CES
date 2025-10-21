def will_it_fly(q,w):
    print('[LINE]1[/LINE] may be hit')
    if sum(q) > w:
        print('[LINE]1[/LINE] is hit')
        return False

    i, j = 0, len(q)-1
    while i<j:
        print('[LINE]6[/LINE] may be hit')
        if q[i] == q[j]:
            print('[LINE]6[/LINE] is hit')
            return False
        i+=1
        j-=1
    return True

will_it_fly([3, 2, 3], 9)
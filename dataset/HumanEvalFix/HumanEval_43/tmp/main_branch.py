def pairs_sum_to_zero(l):
    for i, l1 in enumerate(l):
        for j in range(i, len(l)):
            print('[LINE]3[/LINE] may be hit')
            if l1 + l[j] == 0:
                print('[LINE]3[/LINE] is hit')
                return True
    return False

pairs_sum_to_zero([1, 3, 5, 0])
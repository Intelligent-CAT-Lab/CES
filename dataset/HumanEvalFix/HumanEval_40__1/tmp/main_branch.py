def triples_sum_to_zero(l: list):
    for i in range(1, len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                print('[LINE]4[/LINE] may be hit')
                if l[i] + l[j] + l[k] == 0:
                    print('[LINE]4[/LINE] is hit')
                    return True
    return False

triples_sum_to_zero([2, 4, (- 5), 3, 9, 7])
def count_nums(arr):
    def digits_sum(n):
        neg = 1
        print('[LINE]3[/LINE] may be hit')
        if n < 0: 
            print('[LINE]3[/LINE] is hit')
            n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg * -1
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))

count_nums([1, 6, 9, (- 6), 0, 1, 5])
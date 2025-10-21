def intersection(interval1, interval2):
    def is_prime(num):
        print('[LINE]2[/LINE] may be hit')
        if num == 1 or num == 0:
            print('[LINE]2[/LINE] is hit')
            return False
        print('[LINE]4[/LINE] may be hit')
        if num == 2:
            print('[LINE]4[/LINE] is hit')
            return True
        for i in range(2, num):
            print('[LINE]7[/LINE] may be hit')
            if num%i == 0:
                print('[LINE]7[/LINE] is hit')
                return False
        return True

    l = max(interval1[0], interval2[0])
    r = min(interval1[1], interval2[1])
    length = r - l
    print('[LINE]14[/LINE] may be hit')
    if length > 0:
        print('[LINE]14[/LINE] is hit')
        return "YES"
    return "NO"

intersection(((- 1), 1), (0, 4))
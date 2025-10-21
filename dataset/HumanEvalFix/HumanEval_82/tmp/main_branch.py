def prime_length(string):
    l = len(string)
    print('[LINE]2[/LINE] may be hit')
    if l == 0 or l == 1:
        print('[LINE]2[/LINE] is hit')
        return False
    for i in range(3, l):
        print('[LINE]5[/LINE] may be hit')
        if l % i == 0:
            print('[LINE]5[/LINE] is hit')
            return False
    return True

prime_length('gogo')
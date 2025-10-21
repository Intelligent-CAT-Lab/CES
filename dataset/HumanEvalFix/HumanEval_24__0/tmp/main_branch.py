def largest_divisor(n: int) -> int:
    for i in reversed(range(n)):
        print('[LINE]2[/LINE] may be hit')
        if n - i == 0:
            print('[LINE]2[/LINE] is hit')
            return i

largest_divisor(49)
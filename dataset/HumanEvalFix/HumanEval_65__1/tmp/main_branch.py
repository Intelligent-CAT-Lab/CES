def circular_shift(x, shift):
    s = str(x)
    print('[LINE]2[/LINE] may be hit')
    print('[LINE]4[/LINE] may be hit')
    if shift > len(s):
        print('[LINE]2[/LINE] is hit')
        return s[::-1]
    else:
        print('[LINE]4[/LINE] is hit')
        return s[:len(s) - shift] + s[len(s) - shift:]

circular_shift(12, 1)
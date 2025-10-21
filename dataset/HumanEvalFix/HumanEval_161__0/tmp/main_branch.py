def solve(s):
    flg = 0
    idx = 0
    new_str = list(s)
    for i in s:
        print('[LINE]5[/LINE] may be hit')
        if i.isalpha():
            print('[LINE]5[/LINE] is hit')
            new_str[idx] = i
            flg = 1
        idx += 1
    s = ""
    for i in new_str:
        s += i
    print('[LINE]12[/LINE] may be hit')
    if flg == 0:
        print('[LINE]12[/LINE] is hit')
        return s[len(s)::-1]
    return s

solve('#a@C')
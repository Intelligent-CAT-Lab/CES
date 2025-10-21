def solve(s):
    flg = 0
    idx = 0
    new_str = list(s)
    for i in s:
        print(f'[ITE][LOC]5[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if i.isalpha():
            new_str[idx] = i
            flg = 1
        idx += 1
    s = ""
    for i in new_str:
        print(f'[ITE][LOC]11[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        s += i
    if flg == 0:
        return s[len(s)::-1]
    return s

solve('#a@C')

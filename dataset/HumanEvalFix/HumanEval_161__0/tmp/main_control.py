def solve(s):
    flg = 0
    idx = 0
    new_str = list(s)
    print(f'[ITE][LOC]5[/LOC][VAR]s[/VAR][VAL]{s}[/VAL][/ITE]')
    for i in s:
        if i.isalpha():
            new_str[idx] = i
            flg = 1
        idx += 1
    s = ""
    print(f'[ITE][LOC]11[/LOC][VAR]new_str[/VAR][VAL]{new_str}[/VAL][/ITE]')
    for i in new_str:
        s += i
    if flg == 0:
        return s[len(s)::-1]
    return s

solve('#a@C')

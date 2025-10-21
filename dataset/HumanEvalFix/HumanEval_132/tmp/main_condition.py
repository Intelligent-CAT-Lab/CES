def is_nested(string):
    opening_bracket_index = []
    closing_bracket_index = []
    for i in range(len(string)):
        print(f"[ITE][LOC]4[/LOC][VAR]string[i] == '('[/VAR][VAL]{string[i] == '('}[/VAL][/ITE]")
        if string[i] == '(':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx in opening_bracket_index:
        print(f'[ITE][LOC]13[/LOC][VAR]i < l and idx < closing_bracket_index[i][/VAR][VAL]{i < l and idx < closing_bracket_index[i]}[/VAL][/ITE]')
        print(f'[ITE][LOC]13[/LOC][VAR]i < l[/VAR][VAL]{i < l}[/VAL][/ITE]')
        print(f'[ITE][LOC]13[/LOC][VAR]idx < closing_bracket_index[i][/VAR][VAL]{idx < closing_bracket_index[i]}[/VAL][/ITE]')
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
    return cnt >= 2

    

is_nested('[[]]')

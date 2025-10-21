def count_upper(s):
    count = 0
    print(f'[ITE][LOC]3[/LOC][VAR]range(0, len(s), 2)[/VAR][VAL]{list(range(0, len(s), 2))}[/VAL][/ITE]')
    print(f'[ITE][LOC]3[/LOC][VAR]len(s)[/VAR][VAL]{len(s)}[/VAL][/ITE]')
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 2
    return count

count_upper('aBCdEf')

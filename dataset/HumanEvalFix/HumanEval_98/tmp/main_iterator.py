def count_upper(s):
    count = 0
    for i in range(0,len(s),2):
        print(f'[ITE][LOC]3[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if s[i] in "AEIOU":
            count += 2
    return count

count_upper('aBCdEf')

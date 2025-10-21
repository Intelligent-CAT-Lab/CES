from typing import *
def count_upper(s):
    count = 0
    for i in range(0,len(s),2):
        print(f'[ITE][LOC]4[/LOC][VAR]i[/VAR][VAL]{i}[/VAL][/ITE]')
        if s[i] in "AEIOU":
            count += 1
    return count

count_upper('aBCdEf')  
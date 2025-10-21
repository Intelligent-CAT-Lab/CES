from typing import *
def count_upper(s):
    count = 0
    for i in range(0,len(s),2):
        print(f'[ITE][LOC]4[/LOC][VAR]s[i] in "AEIOU"[/VAR][VAL]{s[i] in "AEIOU"}[/VAL][/ITE]')
        if s[i] in "AEIOU":
            count += 1
    return count

count_upper('aBCdEf')  
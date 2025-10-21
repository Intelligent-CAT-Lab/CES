from typing import *
def count_upper(s):
    count = 0
    for i in range(0,len(s),2):
        print('[LINE]4[/LINE] may be hit')
        if s[i] in "AEIOU":
            print('[LINE]4[/LINE] is hit')
            count += 1
    return count

count_upper('aBCdEf')  
def count_upper(s):
    count = 0
    for i in range(0,len(s),2):
        print('[LINE]3[/LINE] may be hit')
        if s[i] in "AEIOU":
            print('[LINE]3[/LINE] is hit')
            count += 2
    return count

count_upper('aBCdEf')
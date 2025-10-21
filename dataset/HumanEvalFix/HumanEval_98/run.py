def count_upper(s):
    count = 0
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 2
    return count

output = count_upper('aBCdEf')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_98/output.txt", 'w')
file.write(str(output))
file.close()
    
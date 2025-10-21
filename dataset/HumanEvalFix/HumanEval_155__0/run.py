def even_odd_count(num):
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
    return (even_count, odd_count)

output = even_odd_count((- 345821))

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_155__0/output.txt", 'w')
file.write(str(output))
file.close()
    
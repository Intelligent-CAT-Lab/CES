def prime_length(string):
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(3, l):
        if l % i == 0:
            return False
    return True

output = prime_length('gogo')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_82/output.txt", 'w')
file.write(str(output))
file.close()
    
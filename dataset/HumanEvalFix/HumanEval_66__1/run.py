def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.islower() else 0 for char in s)

output = digitSum('aAaaaXa')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_66__1/output.txt", 'w')
file.write(str(output))
file.close()
    
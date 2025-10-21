def multiply(a, b):
    return abs(a % 10) * abs(b % 10) * a * b

output = multiply(76, 67)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_97__1/output.txt", 'w')
file.write(str(output))
file.close()
    
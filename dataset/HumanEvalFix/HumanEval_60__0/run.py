def sum_to_n(n: int):
    return sum(range(n))

output = sum_to_n(6)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_60__0/output.txt", 'w')
file.write(str(output))
file.close()
    
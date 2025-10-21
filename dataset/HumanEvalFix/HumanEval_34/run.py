def unique(l: list):
    return sorted(l)

output = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_34/output.txt", 'w')
file.write(str(output))
file.close()
    
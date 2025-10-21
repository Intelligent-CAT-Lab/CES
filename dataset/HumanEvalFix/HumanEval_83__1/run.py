def starts_one_ends(n):
    if n == 1: return 1
    return 18 * n * (10 ** (n - 2))

output = starts_one_ends(2)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_83__1/output.txt", 'w')
file.write(str(output))
file.close()
    
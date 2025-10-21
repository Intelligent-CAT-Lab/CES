def incr_list(l: list):
    return [(e + 2) for e in l]

output = incr_list([5, 2, 5, 2, 3, 3, 9, 0, 123])

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_42/output.txt", 'w')
file.write(str(output))
file.close()
    
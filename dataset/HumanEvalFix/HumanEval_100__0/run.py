def make_a_pile(n):
    return [n + 2*i + i for i in range(n)]

output = make_a_pile(4)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_100__0/output.txt", 'w')
file.write(str(output))
file.close()
    
def pairs_sum_to_zero(l):
    for i, l1 in enumerate(l):
        for j in range(i, len(l)):
            if l1 + l[j] == 0:
                return True
    return False

output = pairs_sum_to_zero([1, 3, 5, 0])

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_43/output.txt", 'w')
file.write(str(output))
file.close()
    
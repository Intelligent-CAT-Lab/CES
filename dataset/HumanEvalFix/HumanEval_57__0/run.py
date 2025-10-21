def monotonic(l: list):
    if l == sorted(l) or l == sorted(l, reverse=True):
        return False
    return True

output = monotonic([4, 1, 0, (- 10)])

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_57__0/output.txt", 'w')
file.write(str(output))
file.close()
    
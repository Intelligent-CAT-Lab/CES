def max_element(l: list):
    m = l[0]
    for e in l:
        if e < m:
            m = e
    return m

output = max_element([1, 2, 3])

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_35/output.txt", 'w')
file.write(str(output))
file.close()
    
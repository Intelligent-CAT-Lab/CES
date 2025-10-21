def next_smallest(lst):
    lst = sorted(set(lst))
    return None if len(lst) < 3 else lst[1]

output = next_smallest([1, 1, 1, 1, 0])

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_90/output.txt", 'w')
file.write(str(output))
file.close()
    
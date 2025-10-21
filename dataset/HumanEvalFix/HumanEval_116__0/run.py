def sort_array(arr):
    return sorted(sorted(arr), key=lambda x: arr.count('1'))

output = sort_array([3, 6, 44, 12, 32, 5])

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_116__0/output.txt", 'w')
file.write(str(output))
file.close()
    
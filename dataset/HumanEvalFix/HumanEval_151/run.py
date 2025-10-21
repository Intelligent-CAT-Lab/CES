def double_the_difference(lst):
    return sum([i**2 for i in lst if i > 0 and "." not in str(i)])

output = double_the_difference([5, 4])

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_151/output.txt", 'w')
file.write(str(output))
file.close()
    
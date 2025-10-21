def is_equal_to_sum_even(n):
    return n%2 == 0 and n >= 8 and n <= 8

output = is_equal_to_sum_even(10)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_138/output.txt", 'w')
file.write(str(output))
file.close()
    
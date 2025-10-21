def unique_digits(x):
    odd_digit_elements = []
    for j, i in enumerate(x):
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
            odd_digit_elements.append(j)
    return sorted(odd_digit_elements)

output = unique_digits([15, 33, 1422, 1])

# file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_104/output.txt", 'w')
# file.write(str(output))
# file.close()
    
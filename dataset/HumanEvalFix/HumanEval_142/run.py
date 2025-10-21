def sum_squares(lst):
    result =[]
    for i in range(len(lst)):
        if i %3 == 0:
            result.append(lst[i]**2)
        elif i%3 != 0:
            result.append(lst[i]**3)
        else:
            result.append(lst[i])
    print(result)
    return sum(result)

output = sum_squares([1, 2, 3])
print(output)
# file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_142/output.txt", 'w')
# file.write(str(output))
# file.close()
    
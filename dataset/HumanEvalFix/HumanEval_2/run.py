def truncate_number(number: float) -> float:
    return number % 1.0 + 1.0

output = truncate_number(3.5)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_2/output.txt", 'w')
file.write(str(output))
file.close()
    
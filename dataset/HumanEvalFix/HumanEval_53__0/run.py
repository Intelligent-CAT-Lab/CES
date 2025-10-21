def add(x: int, y: int):
    return x + y + y + x

output = add(7, 5)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_53__0/output.txt", 'w')
file.write(str(output))
file.close()
    
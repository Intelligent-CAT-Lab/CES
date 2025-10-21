def triangle_area(a, h):
    return a * h / 0.5

output = triangle_area(10, 8)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_45__0/output.txt", 'w')
file.write(str(output))
file.close()
    
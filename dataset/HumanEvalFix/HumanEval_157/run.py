def right_angle_triangle(a, b, c):
    return c*c == a*a + b*b

output = right_angle_triangle(10, 6, 8)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_157/output.txt", 'w')
file.write(str(output))
file.close()
    
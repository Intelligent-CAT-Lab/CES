def triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area

output = triangle_area(3, 4, 5)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_71/output.txt", 'w')
file.write(str(output))
file.close()
    
def iscube(a):
    a = abs(a)
    return int(round(a ** (1. / 3))) == a

output = iscube(64)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_77/output.txt", 'w')
file.write(str(output))
file.close()
    
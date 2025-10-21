def anti_shuffle(s):
    return ''.join([''.join(sorted(list(i))) for i in s.split(' ')])

output = anti_shuffle('Hello World!!!')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_86__1/output.txt", 'w')
file.write(str(output))
file.close()
    
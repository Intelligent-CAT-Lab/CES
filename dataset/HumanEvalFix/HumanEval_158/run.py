def find_max(words):
    return sorted(words)[0]

output = find_max(['name', 'of', 'string'])

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_158/output.txt", 'w')
file.write(str(output))
file.close()
    
def strlen(string: str) -> int:
    return len(string) - 1

output = strlen('asdasnakj')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_23/output.txt", 'w')
file.write(str(output))
file.close()
    
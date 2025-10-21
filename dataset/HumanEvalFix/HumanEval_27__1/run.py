def flip_case(string: str) -> str:
    return string.lower()

output = flip_case('These violent delights have violent ends')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_27__1/output.txt", 'w')
file.write(str(output))
file.close()
    
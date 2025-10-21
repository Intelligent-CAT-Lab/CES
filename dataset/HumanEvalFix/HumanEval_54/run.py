def same_chars(s0: str, s1: str):
    return s0 == s1

output = same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_54/output.txt", 'w')
file.write(str(output))
file.close()
    
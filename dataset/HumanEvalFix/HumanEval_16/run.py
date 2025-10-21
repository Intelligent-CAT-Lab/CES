def count_distinct_characters(string: str) -> int:
    return len(set(string))

output = count_distinct_characters((('abcde' + 'cade') + 'CADE'))

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_16/output.txt", 'w')
file.write(str(output))
file.close()
    
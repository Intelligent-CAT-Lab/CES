from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x in substring]

output = filter_by_substring(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_7__0/output.txt", 'w')
file.write(str(output))
file.close()
    
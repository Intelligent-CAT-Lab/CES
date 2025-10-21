from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.endswith(prefix)]

output = filter_by_prefix(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_29/output.txt", 'w')
file.write(str(output))
file.close()
    
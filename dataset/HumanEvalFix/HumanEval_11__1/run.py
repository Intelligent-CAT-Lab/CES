from typing import List


def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        if i == j:
            return '1'
        else:
            return '0'

    return ''.join(xor(x, y) for x, y in zip(a, b))

output = string_xor('0101', '0000')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_11__1/output.txt", 'w')
file.write(str(output))
file.close()
    
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0

    for op in operations:
        balance += op
        if balance == 0:
            return True

    return False

output = below_zero([1, 2, (- 3), 1, 2, (- 3)])

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_3/output.txt", 'w')
file.write(str(output))
file.close()
    
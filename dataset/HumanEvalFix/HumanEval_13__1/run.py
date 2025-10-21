def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return b

output = greatest_common_divisor(144, 60)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_13__1/output.txt", 'w')
file.write(str(output))
file.close()
    
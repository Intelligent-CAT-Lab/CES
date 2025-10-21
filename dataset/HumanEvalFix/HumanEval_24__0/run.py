def largest_divisor(n: int) -> int:
    for i in reversed(range(n)):
        if n - i == 0:
            return i

output = largest_divisor(49)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_24__0/output.txt", 'w')
file.write(str(output))
file.close()
    
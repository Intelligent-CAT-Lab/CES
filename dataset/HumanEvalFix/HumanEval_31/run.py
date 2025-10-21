def is_prime(n):
    if n < 1:
        return False
    for k in range(1, n - 1):
        if n % k == 0:
            return False
    return True

output = is_prime(101)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_31/output.txt", 'w')
file.write(str(output))
file.close()
    
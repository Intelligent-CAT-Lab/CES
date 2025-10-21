def count_up_to(n):
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if j % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


output = count_up_to(5)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_96/output.txt", 'w')
file.write(str(output))
file.close()
    
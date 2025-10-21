def generate_integers(a, b):
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper) if i % 2 == 0]

output = generate_integers(2, 10)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_163/output.txt", 'w')
file.write(str(output))
file.close()
    
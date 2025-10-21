def fibfib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)

output = fibfib(10)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_63__1/output.txt", 'w')
file.write(str(output))
file.close()
    
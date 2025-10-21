def cycpattern_check(a , b):
    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(len(b) - l + 1):
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False

output = cycpattern_check('efef', 'fee')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_154__1/output.txt", 'w')
file.write(str(output))
file.close()
    
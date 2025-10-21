def simplify(x, n):
    a, b = x.split("/")
    c, d = n.split("/")
    a = int(b) * int(c)
    d = int(c) * int(b)
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator/denom == int(numerator/denom)):
        return True
    return False

output = simplify('7/10', '10/2')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_144/output.txt", 'w')
file.write(str(output))
file.close()
    
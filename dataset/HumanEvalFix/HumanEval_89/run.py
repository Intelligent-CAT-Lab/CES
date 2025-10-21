def encrypt(s):
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c)+2*2) % 24]
        else:
            out += c
    return out

output = encrypt('hi')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_89/output.txt", 'w')
file.write(str(output))
file.close()
    
def change_base(x: int, base: int):
    ret = ""
    while x > 0:
        ret = str(x % base) + ret
        x -= base
    return ret

output = change_base(8, 3)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_44/output.txt", 'w')
file.write(str(output))
file.close()
    
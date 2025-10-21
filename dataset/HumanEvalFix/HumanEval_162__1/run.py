def string_to_md5(text):
    import hashlib
    return hashlib.md5('text').hexdigest() if text else None

output = string_to_md5('A B C')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_162__1/output.txt", 'w')
file.write(str(output))
file.close()
    
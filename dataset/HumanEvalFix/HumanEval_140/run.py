def fix_spaces(text):
    new_text = ""
    i = 0
    start, end = 0, 0
    while i < len(text):
        if text[i] == " ":
            end += 1
        else:
            if end - start > 2:
                new_text += "-"+text[i]
            elif end - start > 0:
                new_text += "_"*(end - start)+text[i]
            else:
                new_text += text[i]
            start, end = i+1, i+1
        i+=1
    if end - start > 2:
        new_text += "-"
    elif end - start > 0:
        new_text += "__"
    return new_text

output = fix_spaces('Mudasir Hanif ')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_140/output.txt", 'w')
file.write(str(output))
file.close()
    
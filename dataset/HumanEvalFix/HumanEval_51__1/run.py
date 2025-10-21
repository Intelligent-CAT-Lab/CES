def remove_vowels(text):
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u", "w", "y"]])

output = remove_vowels('ybcd')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_51__1/output.txt", 'w')
file.write(str(output))
file.close()
    
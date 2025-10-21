FIX = """
Add more test cases.
"""

def vowels_count(s):
    vowels = "aeiouyAEIOUY"
    n_vowels = sum(c in vowels for c in s)
    return n_vowels

output = vowels_count('bYe')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_64__0/output.txt", 'w')
file.write(str(output))
file.close()
    
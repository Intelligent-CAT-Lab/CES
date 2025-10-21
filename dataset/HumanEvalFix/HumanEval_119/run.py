def match_parens(lst):
    def check(s):
        val = 0
        for i in s:
            if i == '(':
                val = val + 1
            else:
                val = val - 1
            if val < 0:
                return False
        return True if val == 0 else False

    S1 = lst[0] + lst[1]
    S2 = lst[1] + lst[0]
    return 'yes' if check(S1) or check(S2) else 'no'

output = match_parens(['()(', ')'])

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_119/output.txt", 'w')
file.write(str(output))
file.close()
    
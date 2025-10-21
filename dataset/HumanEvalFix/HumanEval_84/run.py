def solve(N):
    return bin([int(i) for i in str(N)][-1])[2:]

output = solve(1000)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_84/output.txt", 'w')
file.write(str(output))
file.close()
    
def solution(lst):
    return sum([x for idx, x in enumerate(lst) if idx%2==1 and x%2==1])

output = solution([5, 8, 7, 1])

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_121/output.txt", 'w')
file.write(str(output))
file.close()
    
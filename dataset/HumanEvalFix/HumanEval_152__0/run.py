def compare(game,guess):
    return [abs(x-y)+abs(y-x) for x,y in zip(game,guess)]

output = compare([1, 2, 3, 5], [(- 1), 2, 3, 4])

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_152__0/output.txt", 'w')
file.write(str(output))
file.close()
    
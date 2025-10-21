def get_row(lst, x):
    coords = [(j, i) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])

output = get_row([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_87/output.txt", 'w')
file.write(str(output))
file.close()
    
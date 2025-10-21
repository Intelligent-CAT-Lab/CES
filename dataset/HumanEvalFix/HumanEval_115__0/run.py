def max_fill(grid, capacity):
    import math
    return sum([math.floor(sum(arr)/capacity) for arr in grid])

output = max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_115__0/output.txt", 'w')
file.write(str(output))
file.close()
    
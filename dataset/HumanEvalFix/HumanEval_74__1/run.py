def total_match(lst1, lst2):
    l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    if l1 <= l2:
        return lst2
    else:
        return lst1

output = total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project'])

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_74__1/output.txt", 'w')
file.write(str(output))
file.close()
    
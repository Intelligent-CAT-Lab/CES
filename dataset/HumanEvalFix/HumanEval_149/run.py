def sorted_list_sum(lst):
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i)%2 == 0:
            new_lst.append(i)
    return new_lst

output = sorted_list_sum(['aaaa', 'bbbb', 'dd', 'cc'])

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_149/output.txt", 'w')
file.write(str(output))
file.close()
    
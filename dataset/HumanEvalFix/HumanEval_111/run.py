def histogram(test):
    dict1={}
    list1=test.split(" ")
    t=1

    for i in list1:
        if(list1.count(i)>t) and i!='':
            t=list1.count(i)
    if t>0:
        for i in list1:
            if(list1.count(i)==t):
                
                dict1[i]=t
    return dict1

output = histogram('')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_111/output.txt", 'w')
file.write(str(output))
file.close()
    
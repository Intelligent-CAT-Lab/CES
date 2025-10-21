def eat(number, need, remaining):
    if(need <= remaining):
        return [ number + need , number + remaining-need ]
    else:
        return [ number + need + remaining , 0]

output = eat(2, 11, 5)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_159__1/output.txt", 'w')
file.write(str(output))
file.close()
    
def decimal_to_binary(decimal):
    return "db" + bin(decimal)[2:] + "d"

output = decimal_to_binary(103)

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_79__1/output.txt", 'w')
file.write(str(output))
file.close()
    
def how_many_times(string: str, substring: str) -> int:
    times = 0

    for i in range(len(string) - len(substring)):
        print(string[i:i+len(substring)] == substring)
        if string[i:i+len(substring)] == substring:
            times += 1
    print(times)
    return times

output = how_many_times('xyxyxyx', 'x')

# file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_18__0/output.txt", 'w')
# file.write(str(output))
# file.close()
    
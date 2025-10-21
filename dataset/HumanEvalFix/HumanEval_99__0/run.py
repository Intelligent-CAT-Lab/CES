def closest_integer(value):
    from math import floor, ceil

    if value.count('.') == 1:
        # remove trailing zeros
        while (value[-1] == '0'):
            value = value[:-1]

    num = float(value)
    if value[-2:] == '.5':
        if num > 0:
            res = floor(num)
        else:
            res = ceil(num)
    elif len(value) > 0:
        res = int(round(num))
    else:
        res = 0

    return res


output = closest_integer('14.5')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_99__0/output.txt", 'w')
file.write(str(output))
file.close()
    
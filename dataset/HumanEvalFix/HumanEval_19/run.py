from typing import List


def sort_numbers(numbers: str) -> str:
    value_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    return ' '.join([x for x in numbers.split(' ') if x])

output = sort_numbers('five zero four seven nine eight')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_19/output.txt", 'w')
file.write(str(output))
file.close()
    
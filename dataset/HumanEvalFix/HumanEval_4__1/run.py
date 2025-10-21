from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / mean

output = abs((mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]) - (6.0 / 5.0)))

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_4__1/output.txt", 'w')
file.write(str(output))
file.close()
    
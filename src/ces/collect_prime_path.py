import re
import os

def extract_prime_path():
    root = "/home/changshu/CODEMIND/dataset/humaneval"
    pattern = r'\d+%'
    coverage_set = {}
    for d in os.listdir(root):
        coverage_path = os.path.join(root, d, 'coverage.txt')
        coverage_text = open(coverage_path, 'r').readlines()
        for line in coverage_text:
            if line.startswith("TOTAL"):
                result = re.findall(pattern, line)
        coverage_set[d] = result[0]
    
    return coverage_set

def find_strong():
    covs = extract_prime_path()
    count = 0
    results = {}
    for k in covs:
        k_base = k.split("__")[0]
        if k_base not in results:
            results[k_base] = []
        results[k_base].append(covs[k])
    for k in results:
        if len(set(results[k])) > 1:
            count += 1
    print(count/164)
# find_strong()
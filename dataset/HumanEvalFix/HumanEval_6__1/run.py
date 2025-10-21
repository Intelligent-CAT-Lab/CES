from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    def parse_paren_group(s):
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(depth, max_depth)
            else:
                max_depth -= 1
            print(c, depth, max_depth)
        return max_depth
    return [parse_paren_group(x) for x in paren_string.split(' ') if x]

output = parse_nested_parens('(()(())((())))')

# file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_6__1/output.txt", 'w')
# file.write(str(output))
# file.close()
    
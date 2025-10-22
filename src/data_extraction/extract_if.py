import ast
from pathlib import Path
import json
import argparse

class IfExtractor(ast.NodeVisitor):
    def __init__(self):
        self.if_statements = []

    def visit_If(self, node):
        self.if_statements.append(node)  # Collect the if statement
        self.generic_visit(node)  # Continue traversing to find nested if statements


def extract_if_statements(source_code):
    tree = ast.parse(source_code)
    extractor = IfExtractor()
    extractor.visit(tree)
    return extractor.if_statements

def parse_if_node(node, index_list):
    index_list.append(node.test.lineno-1)
    if len(node.orelse) > 0:
        if isinstance(node.orelse[0], ast.If):
            parse_if_node(node.orelse[0], index_list)
        else:
            index_list.append(node.orelse[0].lineno-2) 

def is_sublist_any_order(list1, list2):
    return all(item in list1 for item in list2)

def main(file_path):
    source_code = open(file_path, 'r').read()
    if_statements = extract_if_statements(source_code)
    candidate_list = []
    cleaned_list = []
    for stmt in if_statements:
        lineno = []
        parse_if_node(stmt, lineno)
        candidate_list.append(lineno)
    for c in candidate_list:
        flag = True
        for a in cleaned_list:
            if all(item in a for item in c):
                flag = False
                break
            elif all(item in c for item in a):
                cleaned_list.remove(a)
                break
        if flag:
            cleaned_list.append(c)
    return cleaned_list
                
                
    return candidate_list

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, default='none', help="select one from [humaneval, HumanEvalFix, etc.]")
    args = parser.parse_args()
    dataset = args.dataset
    
    results = {}
    root = f"./dataset/{dataset}"
    files = list(Path(root).glob("**/main.py"))
    count = 0
    for f in files:
        problem_id = f.parts[-2]
        conditions = main(f)
        results[problem_id] = conditions
        if conditions:
            count += 1

    result_path = f"./dataset/summary/{dataset}_condition_branch.json"

    with open(result_path, 'w') as wr:
        json.dump(results, wr, indent=4)

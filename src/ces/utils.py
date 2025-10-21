import os
import json
import ast
from tree_sitter import Language, Parser
import shutil

Language.build_library(
  'build/my-languages.so',
  ['tree-sitter-python']  # path to the tree-sitter-pyton repo
)
PY_LANGUAGE = Language('build/my-languages.so', 'python')
parser = Parser()
parser.set_language(PY_LANGUAGE)

def read_loop_data(dataset):
    root = "../../dataset/extract"
    iterator_path = os.path.join(root, f"{dataset}_loop.json")
    condition_path = os.path.join(root, f"{dataset}_control.json")
    iterator_data = json.load(open(iterator_path, 'r'))
    control_data = json.load(open(condition_path, 'r'))
    cleaned_data = {}
    for k in control_data.keys():
        cleaned_data[k] = {
            'iterator':{},
            'control':{},
            'all':{}
        }
        
        if k in iterator_data:
            ## append iterators for FOR loops
            for i in iterator_data[k]['For']:
                lineno = i['line_no']
                iterators = i["iterator"]
                iterator_gts = i["iterator_gt"]
                cleaned_data[k]['iterator'][lineno] = {}
                cleaned_data[k]['all'][lineno] = {}
                for ite, ite_gt in zip(iterators, iterator_gts):
                    cleaned_data[k]['iterator'][lineno][ite] = ite_gt
                    cleaned_data[k]['all'][lineno][ite] = ite_gt
        ## append loop control
        for j in control_data[k]:
            line_no = j["line_no"] - 1
            conditions = j['condition']
            condition_gts = j['condition_gt']
            cleaned_data[k]['control'][line_no] = {}
            if line_no not in cleaned_data[k]['all'].keys():
                cleaned_data[k]['all'][line_no] = {}
            if condition_gts:
                for cond, cond_gt in zip(conditions, condition_gts):
                    cleaned_data[k]['control'][line_no][cond] = cond_gt
                    cleaned_data[k]['all'][line_no][cond] = cond_gt
            else:
                for cond in conditions:
                    cleaned_data[k]['control'][line_no][cond] = []
                    cleaned_data[k]['all'][line_no][cond] = []
    iterator_path = os.path.join(root, f"{dataset}_loop_extended.json")
    condition_path = os.path.join(root, f"{dataset}_control_extended.json")
    iterator_data = json.load(open(iterator_path, 'r'))
    control_data = json.load(open(condition_path, 'r'))
    for k in control_data.keys():
        cleaned_data[k] = {
            'iterator':{},
            'control':{},
            'all':{}
        }
        
        if k in iterator_data:
            ## append iterators for FOR loops
            for i in iterator_data[k]['For']:
                lineno = i['line_no']-1
                iterators = i["iterator"]
                iterator_gts = i["iterator_gt"]
                cleaned_data[k]['iterator'][lineno] = {}
                cleaned_data[k]['all'][lineno] = {}
                for ite, ite_gt in zip(iterators, iterator_gts):
                    cleaned_data[k]['iterator'][lineno][ite] = ite_gt
                    cleaned_data[k]['all'][lineno][ite] = ite_gt
        ## append loop control
        for j in control_data[k]:
            line_no = j["line_no"] - 1
            conditions = j['condition']
            condition_gts = j['condition_gt']
            cleaned_data[k]['control'][line_no] = {}
            if line_no not in cleaned_data[k]['all'].keys():
                cleaned_data[k]['all'][line_no] = {}
            if condition_gts:
                for cond, cond_gt in zip(conditions, condition_gts):
                    cleaned_data[k]['control'][line_no][cond] = cond_gt
                    cleaned_data[k]['all'][line_no][cond] = cond_gt
            else:
                for cond in conditions:
                    cleaned_data[k]['control'][line_no][cond] = []
                    cleaned_data[k]['all'][line_no][cond] = []
                    
    return cleaned_data

def read_condition_data(dataset):
    cleaned_data = {}
    root = "../../dataset/extract"
    condition_path = os.path.join(root, f"{dataset}_condition.json")
    condition_data = json.load(open(condition_path, 'r'))
    for key in condition_data:
        cleaned_data[key] = {}
        for item in condition_data[key]:
            lineno = item['line_no']
            conditions = item['condition']
            gts = item['condition_gt']
            cleaned_data[key][lineno] = {}
            for cond, gt in zip(conditions, gts):
                cleaned_data[key][lineno][cond] = gt
    condition_path = os.path.join(root, f"{dataset}_condition_extended.json")
    condition_data = json.load(open(condition_path, 'r'))
    for key in condition_data:
        cleaned_data[key] = {}
        for item in condition_data[key]:
            lineno = item['line_no']
            conditions = item['condition']
            gts = item['condition_gt']
            cleaned_data[key][lineno] = {}
            for cond, gt in zip(conditions, gts):
                cleaned_data[key][lineno][cond] = gt
      
    return cleaned_data


def read_branch_data(dataset):
    root = "../../dataset/extract"
    branch_path =  os.path.join(root, f"{dataset}_branch.json")
    branch_data=  json.load(open(branch_path, 'r'))
    cleaned_data = {}
    for k in branch_data:
        cleaned_data[k] = {}
        for i in branch_data[k]:
            cleaned_data[k][int(i)] = {"taken":branch_data[k][i]}
    branch_path =  os.path.join(root, f"{dataset}_branch_extended.json")
    branch_data=  json.load(open(branch_path, 'r'))
    for k in branch_data:
        cleaned_data[k] = {}
        for i in branch_data[k]:
            cleaned_data[k][int(i)] = {"taken":branch_data[k][i]}
    return cleaned_data


class LoopFinder(ast.NodeVisitor):
    def __init__(self):
        self.loops = []

    # Method to visit for-loops
    def visit_For(self, node):
        self.loops.append(('For', node.lineno))
        self.generic_visit(node)  # Continue visiting child nodes

    # Method to visit while-loops
    def visit_While(self, node):
        self.loops.append(('While', node.lineno))
        self.generic_visit(node)  # Continue visiting child nodes

class IfFinder(ast.NodeVisitor):
    def __init__(self):
        self.conditions = []
    def visit_If(self, node):
        self.conditions.append(('If', node.lineno))
        self.generic_visit(node)


def get_type(filename):
    with open(filename, "r") as file:
        code = file.read()

    tree = ast.parse(code)
    loop_finder = LoopFinder()
    if_finder = IfFinder()
    loop_finder.visit(tree)
    if_finder.visit(tree)

    if loop_finder.loops and if_finder.conditions:
        return "LC"
    elif loop_finder.loops:
        return "LO"
    elif if_finder.conditions:
        return "CO"
    else:
        return "Other"

def run_query(tree, query_text):
    query = PY_LANGUAGE.query(query_text)
    captures = query.captures(tree.root_node)
    return captures
    

def search_loop(tree):
    ## extract loop structure, return {(start_byte, end_byte):"For/While"}
    query= """
[((for_statement)@for_loop)
(while_statement)@while_loop]
    """
    results = {}
    captures = run_query(tree, query)
    for capture in captures:
        label = capture[1]
        byte_start = capture[0].start_byte
        byte_end = capture[0].end_byte
        position = (byte_start, byte_end)
        results[position] = label
    for k in results.copy():
        for j in results.copy():
            if k != j:
                if k[0]>j[0] and k[1] <= j[1]:
                    ## k in a loop inside j
                    results.pop(k)
                    results[j] = 'nested_loop'
                
    return results

def search_condition(tree):
    ## ectract conditional statement
    query = """
[((if_statement)@if)
(elif_clause)@elif
]
"""
    results = {}
    captures = run_query(tree, query)
    for capture in captures:
        label = capture[1]
        byte_start = capture[0].start_byte
        byte_end = capture[0].end_byte
        position = (byte_start, byte_end)
        results[position] = label
    copy_results = results.copy()
    for k in copy_results:
        for j in copy_results:
            if copy_results[k] == 'elif' and k[0]>j[0] and k[1] <= j[1]:
                if k in results:
                    results.pop(k)
                results[j] = 'else_if'
    ## check nested if
    for k in copy_results:
        for j in copy_results:
            if copy_results[k] == 'if' and copy_results[k] =='if' and k[0]>j[0] and k[1] < j[1]:
                if k in results:
                    results.pop(k)
                results[j] = 'nested_if'
                
            
    return results



def parse_file(file_path):
    file = open(file_path, 'r')
    source_code = file.read()
    tree = parser.parse(bytes(source_code, 'utf-8'))
    loops = search_loop(tree)
    conditions = search_condition(tree)
    label = 'if'
    
    ## case 1. no loop, only conditional statement:
    ## Three possibilities: nested_if >else_if > if
    if not loops and conditions:
        # print(conditions)
        label = "if"
        for k in conditions:
            if conditions[k] == "nested_if":
                label = "nested_if"
            elif conditions[k] == "else_if" and label == "if":
                label = "else_if"
        label = [label]
    ## case 2. no conditions, only loops:
    ## Three possibilities: nested loop > for = while
    elif not conditions and loops:
        label = []
        for k in loops:
            if k not in label:
                label.append(loops[k])
    ## case 3. with conditions and loops. 
    elif loops and conditions:
        flags = []
        for i in loops:
            for k in conditions:
                if k[0]>i[0] and k[1]<=i[1]:
                    flag = f"{conditions[k]} in {loops[i]}"
                    if flag not in flags:
                        flags.append(flag)
        if not flags: ## conditions outside loops
           for i in loops:
            for k in conditions:
                flag = f"{conditions[k]} outside {loops[i]}"
                if flag not in flags:
                    flags.append(flag)
        label = flags
    else:
        label = ["simple"]
    return label
        
def parse_all(root):
    labels= []
    for d in os.listdir(root):
        code_path = os.path.join(root, d, 'main.py')
        # print(code_path)
        r = parse_file(code_path)
        for i in r:
            if i == 'nested_loop':
                print(code_path)
            if i not in labels:
                labels.append(i)
    print(labels)


def clean_folder():
    root = "/home/changshu/CodeMind_Results/results/adaptive_loop_condition_branch_condition_only/deepseek-coder-6.7b-instruct/humaneval"
    for d in os.listdir(root):
        sub_root = os.path.join(root, d)
        for j in os.listdir(sub_root):
            if '__' in j:
                folder = os.path.join(sub_root, j)
                shutil.rmtree(folder)
                
# if __name__ == "__main__":
#     # loop_data = read_branch_data('humaneval')
#     # print(loop_data.keys())
#     filename = "/home/changshu/CODEMIND/dataset/humaneval/HumanEval_4/main.py"
#     r = get_type(filename)
#     print(r)
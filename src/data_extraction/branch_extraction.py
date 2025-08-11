from tree_sitter import Language, Parser
import os
from tqdm import tqdm
import ast
import json
from subprocess import PIPE, Popen
import re
Language.build_library(
  'build/my-languages.so',
  ['tree-sitter-python']  # path to the tree-sitter-pyton repo
)

PY_LANGUAGE = Language('build/my-languages.so', 'python')
parser = Parser()
parser.set_language(PY_LANGUAGE)

def extract_branch(folder_path):
    file_path = os.path.join(folder_path, 'main.py')
    file = open(file_path, 'r')
    source_code = file.read()
    tree = parser.parse(bytes(source_code, 'utf-8'))
    query = PY_LANGUAGE.query("""
(if_statement) @if
(elif_clause) @elif
(else_clause) @else
"""
)
    captures = query.captures(tree.root_node)
    else_elif = {}
    if_set = {}
    cleaned_data = {}
    for capture in captures:
        pos = capture[0].start_point[0]
        if capture[1] == 'if':
            if_set[pos] = (capture[0].start_byte, capture[0].end_byte)
            cleaned_data[pos] = [pos]
        else:
            else_elif[pos] = (capture[0].start_byte, capture[0].end_byte)
    
    for k in else_elif:
        for j in if_set:
            if else_elif[k][0] > if_set[j][0] and else_elif[k][1] <= if_set[j][1]:
                cleaned_data[j].append(k)
                break
    return cleaned_data

def rewrite_py(folder_path, data):
    def get_indentations(line):
        indentations = " "*(len(line)-len(line.lstrip()))
        return indentations
    code_path = os.path.join(folder_path, 'main.py')
    input_path = os.path.join(folder_path, 'input.txt')
    wr_folder = os.path.join(folder_path, 'tmp')
    if not os.path.exists(wr_folder):
        os.mkdir(wr_folder)
    wr_path = os.path.join(folder_path, 'tmp', 'main_branch.py')

    code_input = open(input_path, 'r').read().strip('\n')

    file = open(code_path, 'r')
    new_lines = []
    instrumented_lines = []
    for d in data:
        instrumented_lines.extend(data[d])
    for lineno, line in enumerate(file):
        if lineno not in instrumented_lines:
            new_lines.append(line)
        else:
            ind = get_indentations(line)
            if lineno in data:
                ## insert lines before branches:
                for l in data[lineno]:
                    new_text = f"print('[LINE]{l}[/LINE] may be hit')\n"
                    new_lines.append(ind + new_text)
            new_lines.append(line)
            ## insert lines inside branches
            new_text = f"print('[LINE]{lineno}[/LINE] is hit')\n"
            new_lines.append(ind+"    "+new_text)
    new_lines.append('\n' + code_input)
    new_code = "".join(new_lines)
    with open(wr_path, 'w') as wr:
        wr.write(new_code)       

def extract_all(root):
    results = {}
    for d in os.listdir(root):
        file_path = os.path.join(root, d, 'main.py')
        result = extract_branch(file_path)
        if result:
            results[d] = result
    return results


def execute_python(root):
    # for d in os.listdir(root):
    py_path = os.path.join(root, 'tmp', 'main_branch.py')
    output_path = os.path.join(root, 'tmp', 'branch.txt')
    # print(py_path)
    
    if not os.path.exists(py_path):
        print(py_path)
    cmd_py = f"timeout 10s python {py_path}"

    fout = open(output_path, 'w')
    fout.write('some text, as header of the file\n')
    fout.flush()
    try:
        process = Popen(cmd_py.split(' '), stdout=fout, stdin=PIPE, stderr=PIPE)

        _,error=process.communicate()
        if error:
            print("*"*10)
            print(error)
            print(py_path)
        else:
            pass
            
    except:
        print(py_path)

def parse_file(folder):
    log_path = os.path.join(folder, 'tmp', 'branch.txt')
    file = open(log_path, 'r').read()\
    ## extract all possible branches
    pattern=r"\[LINE\](\d+)\[/LINE\] may be hit"
    matches = re.findall(pattern, file)
    possible_branches = set(matches)
    data= {}
    ## cut the file using "[LINE]x[\LINE] may be hit"
    for pb in possible_branches:
        taken = [] ## 0: miss, 1: hit
        saperator = f"[LINE]{pb}[/LINE] may be hit"
        sections = file.split(saperator)[1:]
        for s in sections:
            if f"[LINE]{pb}[/LINE] is hit" in s:
                taken.append('Y')
            else:
                taken.append('N')ss
        data[int(pb)] = taken
    return data

# a = extract_all("/home/changshu/CODEMIND/dataset/humaneval")
# with open("/home/changshu/CODEMIND/dataset/Loops/huamaneval_branch.json", 'w') as wr:
#     json.dump(a, wr, indent=4)

def main():
    results = {}
    root_humaneval = "dataset/humaneval"
    for d in os.listdir(root_humaneval):
        path = os.path.join(root_humaneval, d)
        data = extract_branch(path)
        if data:
            rewrite_py(path, data)
            execute_python(path)
            r = parse_file(path)
            if r:
                results[d] = r
    # # print(results)
    wr_path_humaneval = "dataset/summary/humaneval_branch.json"
    with open(wr_path_humaneval, 'w') as wr:
        json.dump(results, wr, indent=4)

if __name__ == '__main__':
    main()
from tree_sitter import Language, Parser
import os
from tqdm import tqdm
from subprocess import PIPE, Popen
import ast
import json

Language.build_library(
  'build/my-languages.so',
  ['tree-sitter-python']  # path to the tree-sitter-pyton repo
)

PY_LANGUAGE = Language('build/my-languages.so', 'python')
parser = Parser()
parser.set_language(PY_LANGUAGE)

def get_code_text(code_bytes, node):
    text = code_bytes[node.start_byte: node.end_byte]
    return text

def process_boolean_operator(source_code, node, itemList=[]):
    non_boolean_list = []
    boolean_list = []
    for child in node.children:
        if child.type not in ['and', 'or', 'not', 'boolean_operator', 'parenthesized_expression' ,'(', ')']:
            non_boolean_list.append(child)
        if child.type in ['boolean_operator', 'parenthesized_expression'] :
            boolean_list.append(child)
    for ele in non_boolean_list:
        itemList.append(get_code_text(source_code, ele))
    if len(boolean_list) > 0:
        for ele in boolean_list:
            process_boolean_operator(source_code, ele, itemList)
        return itemList
    else:
        return itemList


def check_condition_type(root):
    types = []
    all_conditions = {} ## {'id':[{line1:[conditions]}, ....}
    for d in os.listdir(root):
        path = os.path.join(root, d, 'main.py')
        with open(path, 'r') as file:
            conditions = []
            source_code = file.read()
            tree = parser.parse(bytes(source_code, "utf8"))
            query = PY_LANGUAGE.query("(if_statement condition:(expression)@condition)")
            captures = query.captures(tree.root_node)
            for capture in captures:
                condition_type = capture[0].type
                condition_text = source_code[capture[0].start_byte:capture[0].end_byte]
                types.append(condition_type)
                items = []
                lineno = capture[0].start_point[0] ## tree-sitter rows are 0-indexed
                if condition_type == "comparison_operator":
                    items.append(condition_text)
                elif condition_type == "parenthesized_expression":
                    for child in capture[0].children:
                        if child.type == "call":
                            code = get_code_text(source_code, child)
                            items.append(code)
                        elif child.type == "boolean_operator":
                            items.append(condition_text)
                            for c in child.children:
                                if c.type not in ['and', 'or', 'not']:
                                    code = get_code_text(source_code, c)
                                    items.append(code)
                        elif child.type == 'comparison_operator':
                            code = get_code_text(source_code, child)
                            items.append(code)
                        elif child.type in ['(' , ')']:
                            pass
                        elif child.type == 'binary_operator':
                            items.append(get_code_text(source_code, child))
                    
                elif condition_type == 'call':
                    items.append(condition_text)
                elif condition_type == 'identifier':
                    items.append(condition_text)
                elif condition_type == 'named_expression':
                    for child in capture[0].children:
                        if child.type == 'identifier':
                            items.append(get_code_text(source_code, child))
                elif condition_type == 'binary_operator':
                    items.append(condition_text)
                elif condition_type == 'boolean_operator':
                    li = process_boolean_operator(source_code, capture[0], [condition_text])
                    items = li
                    pass
                elif condition_type == 'not_operator':
                    items.append(condition_text)
                elif condition_type == 'subscript':
                    items.append(condition_text)
                elif condition_type == 'attribute':
                    items.append(condition_text)
                else:
                    print(condition_text, condition_text, path)
                conditions.append({lineno:items})
            if len(conditions):
                all_conditions[d] = conditions
    return all_conditions

def rewrite_all_py(condition_data, root):
    def rewrite_file(root_folder, condition_set):
        code_path = os.path.join(root_folder, 'main.py')
        input_path = os.path.join(root_folder, 'input.txt')
        if not os.path.exists(code_path) or not os.path.exists(input_path):
            return
        code_input = open(input_path, 'r').read().lstrip()
        new_lines = []
        with open(code_path, 'r') as file:
            lines = file.readlines()
            ## get number of leading spaces:
            for i in range(len(lines)):
                if i in condition_set.keys():
                    if lines[i].startswith('\t'): 
                        leading_space = '\t'* (len(lines[i]) - len(lines[i].lstrip()))
                    else:
                        leading_space = ' '* (len(lines[i]) - len(lines[i].lstrip()))
                    for con in condition_set[i]:
                        if "'" in con:
                            new_line = f'print(f"[ITE][LOC]{i}[/LOC][VAR]{con}[/VAR][VAL]' +"{"+f'{con}'+ "}" +'[/VAL][/ITE]")'
                        else:
                            new_line = f"print(f'[ITE][LOC]{i}[/LOC][VAR]{con}[/VAR][VAL]" +"{"+f'{con}'+ "}" +"[/VAL][/ITE]')"
                        new_lines.append(leading_space + new_line + '\n')
                new_lines.append(lines[i])
        new_code = ''.join(new_lines) + '\n' + code_input
        
        wr_folder = os.path.join(root_folder, 'tmp')
        if not os.path.exists(wr_folder):
            os.makedirs(wr_folder)
        wr_path = os.path.join(wr_folder, 'main_condition.py')
        print(wr_path)
        with open(wr_path, 'w') as wr:
            wr.write(new_code)
        
    for key in condition_data.keys():
        data = condition_data[key]
        cleaned_data = {}
        for i in data:
            for k in i.keys():
                if k not in cleaned_data.keys():
                    cleaned_data[k] = []
                for j in i[k]:
                    cleaned_data[k].append(j)
        # print(root)
        # print(key)
        folder = os.path.join(root, key)
        rewrite_file(folder, cleaned_data)

def execute_python(root):
    for d in os.listdir(root):
        py_path = os.path.join(root, d, 'tmp', 'main_condition.py')
        output_path = os.path.join(root, d, 'tmp', 'condition.txt')
        # print(py_path)
        if not os.path.exists(py_path):
            continue
        else:
            pass
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

def parse_all(root):
    def parse_output_file(path):
        results = {}
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('[ITE]'):
                    lineno = int(line.split('[LOC]')[1].split('[/LOC]')[0])
                    var_name = (line.split('[VAR]')[1].split('[/VAR]')[0])
                    try:
                        var_val = ast.literal_eval(line.split('[VAL]')[1].split('[/VAL]')[0])
                    except:
                        var_val = line.split('[VAL]')[1].split('[/VAL]')[0]
                    if lineno not in results:
                        results[lineno] = {}
                    if var_name not in results[lineno]:
                        results[lineno][var_name] = []
                   
                    results[lineno][var_name].append(var_val)
        converted_results = []
        for k in results:
            obj = {
                'condition': [m for m in results[k].keys()],
                'line_no':k,
                'condition_gt':[]
            }
            for i in results[k]:
                obj['condition_gt'].append(results[k][i])
            converted_results.append(obj)
        return converted_results
    
    if 'Avatar' in root or 'CodeNet' in root or 'cruxeval' in root or 'mbpp' in root or 'humaneval' in root or "HumanEvalFix" in root:
        results = {}
        for d in tqdm(os.listdir(root)):
            # if "__" not in d:
            #     continue
            code_folder = os.path.join(root, d)
            tmp_folder = os.path.join(code_folder, 'tmp')
            if os.path.exists(tmp_folder):
                file_path = os.path.join(tmp_folder, 'condition.txt')
                if not os.path.exists(file_path):
                    continue
                result = parse_output_file(file_path)
                results[d] = result
        if 'humaneval' in root:
            wr_path = f"dataset/summary/humaneval_condition.json"
        if 'HumanEvalFix' in root:
            wr_path = f"dataset/summary/HumanEvalFix_condition.json"
        with open(wr_path, 'w') as wr:
            json.dump(results, wr, indent=4)
            
            
if __name__ == '__main__':
    root_humaneval = "dataset/humaneval" 
    condition_data = check_condition_type(root_humaneval)
    rewrite_all_py(condition_data, root_humaneval)
    execute_python(root_humaneval)
    parse_all(root_humaneval)
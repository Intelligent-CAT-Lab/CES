import ast
import os
import astunparse
import json
import javalang
from subprocess import PIPE, Popen
from tqdm import tqdm
from func_timeout import func_set_timeout
import argparse

class PythonLoopExtractor(ast.NodeVisitor):
    def __init__(self):
        self.loops = {
            'For': [],
            'While': []
        }
    def decompose_control(self, node):
        if isinstance(node, ast.Name):
            return [astunparse.unparse(node).strip('\n')]
        elif isinstance(node, ast.BoolOp):
            items = [astunparse.unparse(node).strip('\n')]
            ## boolean operations:
            ## extract values
            for ele in node.values:
                items.append(astunparse.unparse(ele).strip('\n'))
            return items
        
        elif isinstance(node, ast.Call):
            ## for a function call:
            ## return all the non-constant parameters
            items = [astunparse.unparse(node).strip('\n')]
            for ele in node.args:
                if isinstance(ele, ast.Constant):
                    pass
                elif isinstance(ele, ast.UnaryOp) and isinstance(ele.operand, ast.Constant):
                    pass   
                else:
                    items.append(astunparse.unparse(ele).strip('\n'))
            return items
        
        elif isinstance(node, ast.Compare):
            ## Comparison of values
            ## exclude comparators which are constants
            items = [astunparse.unparse(node).strip('\n')]
            ## left value:
            if isinstance(node.left, ast.Constant):
                pass
            elif isinstance(node.left, ast.UnaryOp) and isinstance(node.left.operand, ast.Constant):
                pass   
            else:
                items.append(astunparse.unparse(node.left).strip('\n'))
            ## other comparators:
            for ele in node.comparators:
                if isinstance(ele, ast.Constant):
                    pass
                elif isinstance(ele, ast.UnaryOp) and isinstance(ele.operand, ast.Constant):
                    pass   
                else:
                    items.append(astunparse.unparse(ele).strip('\n'))
            return items
        
        elif isinstance(node, ast.Constant):
            ## skip constans
            return []
        
        elif isinstance(node, ast.UnaryOp):
            return [astunparse.unparse(node).strip('\n')]
        
        elif isinstance(node, ast.List):
            items = []
            for ele in node.elts:
                if not isinstance(ele, ast.Constant):
                    items.append(astunparse.unparse(ele).strip('\n'))
            return items
        
        elif isinstance(node, ast.Tuple):
            items = []
            for ele in node.elts:
                if not isinstance(ele, ast.Constant):
                    items.append(astunparse.unparse(ele).strip('\n'))
            return items
        
        elif isinstance(node, ast.Subscript):
            return [astunparse.unparse(node).strip('\n')]
        
        elif isinstance(node, ast.ListComp):
            items = []
            items.append(astunparse.unparse(node.elt).strip('\n'))
            # for ele in node.generators:
            #     print(astunparse.unparse(ele).strip('\n'), type(ele))
            # print('*'*10)
            return items
        else:
            print(astunparse.unparse(node), type(node))
            return []
        # print(astunparse.unparse(node).strip('\n'), type(node))


    def visit_For(self, node):
        # print(f"For loop iterating over {ast.dump(node.target)} with iterable {ast.dump(node.iter)}")
        iterators = []
        if isinstance(node.target, ast.Name):
            iterator_name = node.target.id
            iterators.append(iterator_name)
        if isinstance(node.target, ast.Tuple):
            ## multiple iterators
            for iter in node.target.elts:
                if isinstance(iter, ast.Tuple):
                    for j in iter.elts:
                        iterators.append(j.id)
                else:
                    iterators.append(iter.id)
        lno = node.lineno
        iterable = astunparse.unparse(node.iter)
        iterable  = self.decompose_control(node.iter)

        loop_data = {
            'iterator': iterators,
            'condition': iterable,
            'line_no': lno
        }
        self.loops['For'].append(loop_data)      
    
        self.generic_visit(node)

    def visit_While(self, node):
        lno = node.lineno
        condition = astunparse.unparse(node.test)
        condition = self.decompose_control(node.test)
        # print(condition)
        # print(ast.dump(node.test))
        loop_data = {
            'condition': condition,
            'line_no': lno
        }
        self.loops['While'].append(loop_data)
        self.generic_visit(node)

def loop_extraction_py(file_name):
    # print(file_name)
    ## Extract loop iterators and conditions
    # print(file_name)
    code = open(file_name, 'r').read()
    parsed_code = ast.parse(code)
    extractor = PythonLoopExtractor()
    extractor.visit(parsed_code)
    # print(extractor.loops)
    return extractor.loops

def loop_extraction_java(file_name):
    code = open(file_name, 'r').read()
    tree = javalang.parse.parse(code)
    for _, node in tree:
        if isinstance(node, javalang.tree.ForStatement):
            print(node.control)

def rewrite_py(code_path):
    ## add statements to print loop target/iterable
    loop_data = loop_extraction_py(code_path)
    if len(loop_data['For']) > 0:
        cleaned_data = {'For':{},'While':{}}
        for f in loop_data['For']:
            cleaned_data['For'][f['line_no']] = f
        for w in loop_data['While']:
            cleaned_data['While'][w['line_no']] = w
        new_lines = []
        with open(code_path, 'r') as file:
            lines = file.readlines()
            for i in range(len(lines)):
                if 'eval(' in lines[i]:
                    new_lines.append(lines[i].replace('eval', ''))
                else:
                    new_lines.append(lines[i])
                try:
                    if i+1 in cleaned_data['For'].keys():
                        if lines[i+1].startswith('\t'): 
                            leading_space = '\t'* (len(lines[i+1]) - len(lines[i+1].lstrip()))
                        else:
                            leading_space = ' '* (len(lines[i+1]) - len(lines[i+1].lstrip()))
                        ## first print iterators
                        for ite in cleaned_data['For'][(i+1)]['iterator']:
                            new_line = f"print(f'[ITE][LOC]{i+1}[/LOC][VAR]{ite}[/VAR][VAL]" +"{"+f'{ite}'+ "}" +"[/VAL][/ITE]')"
                            new_lines.append(leading_space + new_line + '\n')
                        ## Then print conditions
                    # condition = cleaned_data['For'][(i+1)]['condition'].strip('\n')
                    # new_line = f"print(f'[COND][LOC]{i+1}[/LOC][VAR]{condition}[/VAR][VAL]"+"{"+f'{condition}'+ "}"+"[/VAL][/COND]')"
                    # new_lines.append(leading_space + new_line+'\n')
                except:
                    print(code_path)
                    return
        new_code = ''.join(new_lines)
        if 'cruxeval' in code_path or 'mbpp' in code_path or 'humaneval' in code_path or "HumanEvalFix" in code_path:
            code_folder = '/'.join(code_path.split('/')[:-1])
            input_path = os.path.join(code_folder, 'input.txt')
            code_input = open(input_path, 'r').read()
            new_code = new_code + '\n' + code_input
            
        if 'humaneval' in code_path or "HumanEvalFix" in code_path:
            code_folder = '/'.join(code_path.split('/')[:-1])
            wr_folder = os.path.join(code_folder, 'tmp')
        if 'CodeNet' in code_path:
            code_folder = '/'.join(code_path.split('/')[:-2])
            wr_folder = os.path.join(code_folder, 'tmp')  
        if not os.path.exists(wr_folder):
            os.makedirs(wr_folder)
        wr_path = os.path.join(wr_folder, 'main_iterator.py')
        with open(wr_path, 'w') as wr:
            wr.write(new_code)

def get_leadingspace(lines, i):
    line_with_code = ''
    while True:
        line = lines[i]
        removed_line = line.rstrip('\n')
        if line.startswith('\t'):
            removed_line = line.lstrip('\t').rstrip('\n')
        if line.startswith(' '):
            removed_line = line.lstrip(' ').rstrip('\n')
        
        if removed_line:
            line_with_code = line
            break
        i+=1
    if line_with_code.startswith('\t'):
        leading_space = '\t'* (len(line_with_code) - len(line_with_code.lstrip()))
    else:
        leading_space = ' '* (len(line_with_code) - len(line_with_code.lstrip()))
    return leading_space


def rewrite_py_control(code_path):
    ## add statements to print loop target/iterable
    loop_data = loop_extraction_py(code_path)
    if len(loop_data['For']) > 0 or len(loop_data['While']) > 0:
        cleaned_data = {'For':{},'While':{}}
        for f in loop_data['For']:
            cleaned_data['For'][f['line_no']] = f
        for w in loop_data['While']:
            cleaned_data['While'][w['line_no']] = w
        new_lines = []
        with open(code_path, 'r') as file:
            lines = file.readlines()
            for i in range(len(lines)):
                if 'eval(' in lines[i]:
                    ## taking input from terminal
                    new_lines.append(lines[i].replace('eval', ''))
                # else:
                #     new_lines.append(lines[i])
                try:
                    if i+1 in cleaned_data['For'].keys():
                        leading_space = get_leadingspace(lines, i)
                        
                        # if lines[i+1].startswith('\t'): 
                        #     leading_space = '\t'* (len(lines[i+1]) - len(lines[i+1].lstrip()))
                        # else:
                        #     leading_space = ' '* (len(lines[i+1]) - len(lines[i+1].lstrip()))
                        ## first print iterators
                        # for ite in cleaned_data['For'][(i+1)]['iterator']:
                        #     new_line = f"print(f'[ITE][LOC]{i+1}[/LOC][VAR]{ite}[/VAR][VAL]" +"{"+f'{ite}'+ "}" +"[/VAL][/ITE]')"
                        #     new_lines.append(leading_space + new_line + '\n')
                        ## Then print conditions
                        for condition in cleaned_data['For'][(i+1)]['condition']:
                            if condition.startswith('range(') or condition.startswith('enumerate(') or condition.startswith('zip('):
                                condition_list = "list(" + condition + ")"
                                if "'" in condition:
                                    new_line = f'print(f"[ITE][LOC]{i+1}[/LOC][VAR]{condition}[/VAR][VAL]' +"{"+f'{condition_list}'+ "}" +'[/VAL][/ITE]")'
                                else:
                                    new_line = f"print(f'[ITE][LOC]{i+1}[/LOC][VAR]{condition}[/VAR][VAL]" +"{"+f'{condition_list}'+ "}" +"[/VAL][/ITE]')"
                            else:
                                if "'" in condition:
                                    new_line = f'print(f"[ITE][LOC]{i+1}[/LOC][VAR]{condition}[/VAR][VAL]' +"{"+f'{condition}'+ "}" +'[/VAL][/ITE]")'
                                else:
                                    new_line = f"print(f'[ITE][LOC]{i+1}[/LOC][VAR]{condition}[/VAR][VAL]" +"{"+f'{condition}'+ "}" +"[/VAL][/ITE]')"
                            
                            new_lines.append(leading_space + new_line + '\n')

                    if i+1 in cleaned_data['While'].keys():
                        leading_space = get_leadingspace(lines, i)
                        # if lines[i+1].startswith('\t'): 
                        #     leading_space = '\t'* (len(lines[i+1]) - len(lines[i+1].lstrip()))
                        # else:
                        #     leading_space = ' '* (len(lines[i+1]) - len(lines[i+1].lstrip()))
                        ## first print iterators
                        # for ite in cleaned_data['For'][(i+1)]['iterator']:
                        #     new_line = f"print(f'[ITE][LOC]{i+1}[/LOC][VAR]{ite}[/VAR][VAL]" +"{"+f'{ite}'+ "}" +"[/VAL][/ITE]')"
                        #     new_lines.append(leading_space + new_line + '\n')
                        ## Then print conditions
                        for condition in cleaned_data['While'][(i+1)]['condition']:
                            if condition.startswith('range(') or condition.startswith('enumerate('):
                                condition_list = "list(" + condition + ")"
                                new_line = f"print(f'[ITE][LOC]{i+1}[/LOC][VAR]{condition}[/VAR][VAL]" +"{"+f'{condition_list}'+ "}" +"[/VAL][/ITE]')"
                            else:
                                new_line = f"print(f'[ITE][LOC]{i+1}[/LOC][VAR]{condition}[/VAR][VAL]" +"{"+f'{condition}'+ "}" +"[/VAL][/ITE]')"
                            new_lines.append(leading_space + new_line + '\n')
                    new_lines.append(lines[i])
                except Exception as e:
                    print(e)
                    print(code_path)
                    return
        new_code = ''.join(new_lines)
        if 'cruxeval' in code_path or 'mbpp' in code_path or 'humaneval' in code_path or 'HumanEvalFix' in code_path:
            code_folder = '/'.join(code_path.split('/')[:-1])
            input_path = os.path.join(code_folder, 'input.txt')
            code_input = open(input_path, 'r').read()
            new_code = new_code + '\n' + code_input     
        
        # print(new_code)
        if 'Avatar' in code_path or 'cruxeval' in code_path or 'mbpp' in code_path or 'humaneval' in code_path or "HumanEvalFix":
            code_folder = '/'.join(code_path.split('/')[:-1])
            wr_folder = os.path.join(code_folder, 'tmp')
        if 'CodeNet' in code_path:
            code_folder = '/'.join(code_path.split('/')[:-2])
            wr_folder = os.path.join(code_folder, 'tmp')  
        if not os.path.exists(wr_folder):
            os.makedirs(wr_folder)
        wr_path = os.path.join(wr_folder, 'main_control.py')
        with open(wr_path, 'w') as wr:
            wr.write(new_code)
        


def rewrite_all_python(root):
    if 'Avatar' in root or 'cruxeval' in root or 'mbpp' in root or 'humaneval' in root or 'HumanEvalFix' in root:
        for d in os.listdir(root):
            code_path = os.path.join(root, d, 'main.py')
            rewrite_py(code_path)
            rewrite_py_control(code_path)
    if 'CodeNet' in root:
        for d in os.listdir(root):
            code_path = os.path.join(root, d, 'main', 'main.py')
            rewrite_py(code_path)


def execute_py(code_folder, file_type):
    if 'Avatar' in code_folder or 'CodeNet' in code_folder or 'cruxeval' in code_folder or 'mbpp' in code_folder or 'humaneval' in code_folder or "HumanEvalFix":
        code_path = os.path.join(code_folder, 'tmp', f'main_{file_type}.py')
        output_path = os.path.join(code_folder, 'tmp', f'{file_type}.txt')
        input_path = os.path.join(code_folder, 'input.txt')
    cmd_py = f"timeout 10s python {code_path}"
    if 'Avatar' in code_folder or 'CodeNet' in code_folder:
        code_input = open(input_path, 'r').read()
        code_input = code_input.strip('\n')
        input_bytes = bytes(code_input+'\n', 'utf-8')

    fout = open(output_path, 'w')
    fout.write('some text, as header of the file\n')
    fout.flush()
    try:
        process = Popen(cmd_py.split(' '), stdout=fout, stdin=PIPE, stderr=PIPE)
        if 'Avatar' in code_folder or 'CodeNet' in code_folder:
            process.stdin.write(input_bytes)

        _,error=process.communicate()
        if error:
            print("*"*10)
            print(error)
            print(code_path)
            return 1
        else:
            return 0
    except:
        print(code_path)
        return 1

def execute_all_py(root, file_type):
    count = 0
    if 'Avatar' in root or 'CodeNet' in root or 'cruxeval' in root or 'mbpp' in root or 'humaneval' in root or "HumanEvalFix" in root:
        for d in tqdm(os.listdir(root)):
            code_folder = os.path.join(root, d)
            tmp_folder = os.path.join(code_folder, 'tmp')
            if os.path.exists(tmp_folder):
                r = execute_py(code_folder, file_type)
                count += r
    print(count)
## 
def parse_all_control(root, dataset):
    # @func_set_timeout(10)
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
                    # if var_val not in results[lineno][var_name]: ## filter
                    #     results[lineno][var_name].append(var_val)
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
    
    if 'Avatar' in root or 'CodeNet' in root or 'cruxeval' in root or 'mbpp' in root or 'humaneval' in root or 'HumanEvalFix' in root:
        results = {}
        for d in tqdm(os.listdir(root)):
            code_folder = os.path.join(root, d)
            tmp_folder = os.path.join(code_folder, 'tmp')
            code_path = os.path.join(code_folder, 'main.py')
            if os.path.exists(tmp_folder):
                file_path = os.path.join(tmp_folder, 'control.txt')
                if os.path.exists(file_path):
                    try:
                        result = parse_output_file(file_path)
                        if result == []:
                            
                            loop_data = loop_extraction_py(code_path)
                            for l in loop_data['For']:
                                o = {
                                        "condition": l["condition"],
                                        "line_no": l["line_no"],
                                        "condition_gt": []
                                }
                                result.append(o)
                            for l in loop_data['While']:
                                o = {
                                        "condition": l["condition"],
                                        "line_no": l["line_no"],
                                        "condition_gt": []
                                }
                                result.append(o)                         
                        results[d] = result
                    except:
                        pass
                        # print(d, 'timeout')

        wr_path = f"dataset/summary/{dataset}_control.json"
        with open(wr_path, 'w') as wr:
            json.dump(results, wr, indent=4)



def parse_all_iterator(root, dataset):
    # @func_set_timeout(10)
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
                    # if var_val not in results[lineno][var_name]: ## filter
                    results[lineno][var_name].append(var_val)
        converted_results = []
        for k in results:
            obj = {
                'iterator': [m for m in results[k].keys()],
                'line_no':k,
                'iterator_gt':[]
            }
            for i in results[k]:
                obj['iterator_gt'].append(results[k][i])
            converted_results.append(obj)
        
        return converted_results

    if 'Avatar' in root  or 'cruxeval' in root or 'mbpp' in root or 'humaneval' in root or 'HumanEvalFix' in root:
        results = {}
        for d in tqdm(os.listdir(root)):
            code_folder = os.path.join(root, d)
            tmp_folder = os.path.join(code_folder, 'tmp')
            code_path = os.path.join(code_folder, 'main.py')
            if os.path.exists(tmp_folder):
                file_path = os.path.join(tmp_folder, 'iterator.txt')
                if os.path.exists(file_path):
                    results[d] = {'For':[], 'While':[]}
                    try:
                        result = parse_output_file(file_path)
                        if result == []:
                            loop_data = loop_extraction_py(code_path)
                            for l in loop_data['For']:
                                o = {
                                    "iterator": l["iterator"],
                                    "line_no": l["line_no"],
                                    "iterator_gt": []
                                }
                                result.append(o)
                            
                        
                        results[d]['For']= result 
                    except:
                        pass
                        # print(d, 'timeout')
                

        wr_path = f"dataset/summary/{dataset}_iterator.json"
        with open(wr_path, 'w') as wr:
            json.dump(results, wr, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, default='none', help="select one from [humaneval, HumanEvalFix, etc.]")
    args = parser.parse_args()
    dataset = args.dataset

    root = f'dataset/{dataset}'
    rewrite_all_python(root)
    execute_all_py(root, "control")
    execute_all_py(root, "iterator")
    parse_all_iterator(root, dataset)
    parse_all_control(root, dataset)
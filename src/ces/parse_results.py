import os
import json
import ast
import argparse

def parse_results(file_path, sep_token):
    text = open(file_path, 'r').read()
    if sep_token != 'NA':
        response = text.split(sep_token)[1]
    else:
        response = text
    try:
        if 'deepseek' in file_path or 'Magicoder' in file_path or 'starcoder2-15b' in file_path or 'gemini' in file_path or "semcoder" in file_path or "o4-mini-2025-04-16" in file_path:
            if '[ANSWER]' in response:
                code = response.split("[ANSWER]")[1].split("[/ANSWER]")[0].lstrip("\n")
                if 'PYTHON' in code:
                    code = code.split("[PYTHON]")[1].split("[/PYTHON]")[0].lstrip("\n")
                if "```python" in code:
                    code = code.split("```python")[1].split("```")[0].lstrip("\n")
            elif 'CODE' in response:
                code = code.split("[CODE]")[1].split("[/CODE]")[0].lstrip("\n")
            elif 'PYTHON' in response:
                code = response.split("[PYTHON]")[1].split("[/PYTHON]")[0].lstrip("\n")
            elif '''```python''' in response:
                code = response.split("```python")[1].split("```")[0].lstrip("\n")
                
            # if "__" in file_path:
            #     if not code.startswith("from typing import *"):
            #         code = "from typing import *\n\n\n" + code                
            # else:
            #     if not code.startswith("from typing import *"):
            #         code = "from typing import *\n" + code
            else:
                code = "NA"
                print(file_path)
        elif 'CodeLlama' in file_path or 'gpt' in file_path:
            if "[PYTHON]" in response:
                code = response.split("[PYTHON]")[1].split("[/PYTHON]")[0].lstrip("\n")
            else: 
                code = response.split("```python")[1].split("```")[0].lstrip("\n")
            # if "__" in file_path:
            #     if not code.startswith("from typing import *\n\n\n"):
            #         code = "from typing import *\n\n\n" + "def" + "def".join(code.split("def")[1:])
    except:
        code = "ERROR"
    try:
        reasoning =  response.split("[REASONING]")[1].split("[/REASONING]")[0].lstrip("\n")
    except:
        reasoning = "ERROR"
    try:
        output = response.split("[OUTPUT]")[1].split("[/OUTPUT]")[0].lstrip("\n").lstrip("\n")
    except:
        output = "ERROR"
    root = '/'.join(file_path.split("/")[:-1])
    path_code = os.path.join(root, 'variable.txt')
    path_reasoning = os.path.join(root, 'reasoning.txt')
    path_output = os.path.join(root, 'predict.txt')

    with open(path_code, 'w') as wr_code:
        wr_code.write(code)
    with open(path_reasoning, 'w') as wr_reasoning:
        wr_reasoning.write(reasoning)
    with open(path_output, 'w') as wr_output:
        wr_output.write(output)

def read_loop_data(dataset):
    root = "./dataset/summary"
    root_output = f"./dataset/summary/{dataset}"
    iterator_path = os.path.join(root, f"{dataset}_iterator.json")
    condition_path = os.path.join(root, f"{dataset}_control.json")
    iterator_data = json.load(open(iterator_path, 'r'))
    control_data = json.load(open(condition_path, 'r'))
    cleaned_data = {}
    for k in iterator_data.keys():
        output_path = os.path.join(root_output, k, 'output.txt')
        output = open(output_path, 'r').read().strip('\n') 
        cleaned_data[k] = {
            'iterator':{},
            'control':{},
            'all':{},
            'output': output
        }
        if iterator_data[k]['For']:
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
            for cond, cond_gt in zip(conditions, condition_gts):
                if len(cond_gt) == 1 and isinstance(cond_gt, list):
                    cleaned_data[k]['control'][line_no][cond] = cond_gt[0]
                    cleaned_data[k]['all'][line_no][cond] = cond_gt[0]
                else:
                    cleaned_data[k]['control'][line_no][cond] = cond_gt
                    cleaned_data[k]['all'][line_no][cond] = cond_gt
    return cleaned_data

def parse_all(root):
    for d in os.listdir(root):
        if '.' in d: continue
        response_path = os.path.join(root, d, 'response.txt')
        if not os.path.exists(response_path):
            print(response_path)
            continue
        if 'gpt-4-turbo' in response_path or 'gemini' in response_path or "deepseek-coder-33b-instruct" in response_path or "o4-mini-2025-04-16" in response_path:
            parse_results(response_path, 'NA')
        elif 'deepseek' in response_path:
            parse_results(response_path, "NA")
        elif 'Magicoder' in response_path:
            parse_results(response_path, 'NA')
        elif 'CodeLlama' in response_path:
            parse_results(response_path, 'NA')
        elif 'starcoder2-15b' in response_path:
            parse_results(response_path, 'NA')
        elif 'semcoder' in response_path:
            parse_results(response_path, "NA")




def parse_comments(file_path):
    result = {}
    with open(file_path, 'r') as file:
        for lineno, line in enumerate(file, start=0):
            if "## [STATE]" in line:
                result[lineno] = {}
                comment = line.split("## ")[-1].lstrip()
                for var in comment.split("[/STATE]"):
                    var = var.split("[STATE]")[-1]
                    if '=' not in var:
                        continue
                    v_name = var.split("=")[0]
                    v_value = var.split("=")[1]
                    try:
                        v_value = ast.literal_eval(v_value)
                    except:
                        v_value = v_value
                    result[lineno][v_name] = v_value
    return result


def get_results_variables(root):
    dataset = root.split("/")[-1]
    gt = read_loop_data(dataset)
    def parse_result_single_file(folder):
        variable_flag, output_flag = 0, 0
        program_id = folder.split("/")[-1]
        path_code = os.path.join(folder, 'variable.txt')
        path_output = os.path.join(folder, 'predict.txt')
        result = parse_comments(path_code)
        variable_gt = gt[program_id]['all']
        output_gt = gt[program_id]['output'].lstrip()
        
        if result == variable_gt:
            variable_flag = 1
        
        pred_output = open(path_output, 'r').read().strip('\n').lstrip()
        try:
            pred_output = ast.literal_eval(pred_output)
        except:
            pred_output = pred_output
        try:
            output_gt = ast.literal_eval(output_gt)
        except:
            output_gt = output_gt           
        
        if pred_output == output_gt:
            output_flag = 1
        label = (variable_flag, output_flag)
        
        all_result = {
            'loop_predict':result,
            'loop_gt': variable_gt,
            'output_predict': pred_output,
            'output_gt': output_gt,
            'label': label
        } 
        return all_result
    
    summary = {}
    for d in os.listdir(root):
        if '.json' in d:
            continue
        folder = os.path.join(root, d)
        r = parse_result_single_file(folder)
        summary[d] = r
    
    wr_path = os.path.join(root, 'summary.json')
    with open(wr_path, 'w') as wr:
        json.dump(summary, wr, indent=2, default=lambda x: None)
    


def read_output_data(dataset):
    root_output = f"./dataset/summary/{dataset}"
    outputs = {}
    for d in os.listdir(root_output):
        if '.' in d: continue
        output_path = os.path.join(root_output, d, 'output.txt')
        code_output = open(output_path, 'r').read()
        outputs[d] = code_output
    return outputs

def get_results_output(root):
    dataset = root.split("/")[-1]
    gt = read_output_data(dataset)
    def parse_result_single_file(folder):
        variable_flag, output_flag = 0, 0
        program_id = folder.split("/")[-1]
        path_output = os.path.join(folder, 'predict.txt')

        output_gt = gt[program_id].lstrip()
        
        pred_output = open(path_output, 'r').read().strip('\n').lstrip()
        try:
            pred_output = ast.literal_eval(pred_output)
        except:
            pred_output = pred_output
        try:
            output_gt = ast.literal_eval(output_gt)
        except:
            output_gt = output_gt           
        
        if pred_output == output_gt:
            output_flag = 1
        label = output_flag
        
        all_result = {
            'output_predict': pred_output,
            'output_gt': output_gt,
            'label': label
        } 
        return all_result
    
    summary = {}
    correct_ids = []
    all_id = []
    for d in os.listdir(root):
        all_id.append(d)
        if '.json' in d:
            continue
        folder = os.path.join(root, d)
        r = parse_result_single_file(folder)
        if r['label']==1: correct_ids.append(d)
        summary[d] = r
    
    wr_path = os.path.join(root, 'summary.json')
    with open(wr_path, 'w') as wr:
        json.dump(summary, wr, indent=2, default=lambda x: None)
    return correct_ids, all_id

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default='none')
    parser.add_argument("--dataset", type=str, default='none', help="select one from [humaneval, HumanEvalFix]")
    
    args = parser.parse_args()
    model = args.model
    dataset = args.dataset
    path = f"./Experiment_Results/{model.split('/')[-1]}/{dataset}"
    parse_all(path)
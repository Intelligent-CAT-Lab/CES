import re
from utils import read_loop_data, read_condition_data, read_branch_data, get_type
import json
import ast
import os
import argparse

def convert_value(s):
    try:
        return ast.literal_eval(s)
    except:
        return s

def parse_comments(file_path):
    results = {}
    with open(file_path, 'r') as file:
        for lineno, line in enumerate(file, start=0):
            if "## [STATE]" in line or '## [CONDITION]' in line or '## [BRANCH]' in line:
                results[lineno] = {}
                comment = line.split("## ")[-1].lstrip()
                pattern = r"\[CONDITION](.*?)\[/CONDITION]|\[BRANCH](.*?)\[/BRANCH]|\[STATE](.*?)\[/STATE]"
                matches = re.findall(pattern, comment)
                extracted_values = [item for sublist in matches for item in sublist if item]
                ## extract the key and value
                for item in extracted_values:
                    rhs = item.split("=")[-1]
                    lhs = "=".join(item.split("=")[:-1])
                    # if lhs.startswith('(') and lhs.endswith(")"):
                    #     lhs = lhs[1:-1]
                    results[lineno][lhs] = rhs
    return results


def get_loop_gt(problem_id, loop_data):
    if problem_id not in loop_data:
        return [], []
    gt_iterable, gt_variable = [], []
    for k in loop_data[problem_id]['control']:
        gt_iterable.append({k: loop_data[problem_id]['control'][k]})
        if k in loop_data[problem_id]['iterator']:
            gt_variable.append({k: loop_data[problem_id]['iterator'][k]})
        else:
            gt_variable.append({}) ## possible while loop w/o variable
    return gt_iterable, gt_variable

def get_condition_branch_gt(problem_id, branch_data, condition_data, mapping):
    if problem_id not in condition_data or problem_id not in branch_data:
        return [], []
    condition_all = condition_data[problem_id]
    branch_all = branch_data[problem_id]
    mappings = mapping[problem_id]
    conditions, branches = [], []
    for ids in mappings:
        cond_gt, branch_gt = {}, {}
        for sid in ids:
            if sid in condition_all:
                cond_gt[sid] = condition_all[sid]
            if sid in branch_all:
                branch_gt[sid] = branch_all[sid]
        conditions.append(cond_gt)
        branches.append(branch_gt)
    return conditions, branches

def compare_predict_loop(prediction, gt_variable, gt_iterable):
    labels = {}
    for atom_variable, atom_iterable in zip(gt_variable, gt_iterable):
        ## start from loop variable
        flag_variables, flag_iterables = [], []
        if not atom_variable:
            flag_variables.append(1)
        else:
            for k in atom_variable:
                for v_name in atom_variable[k]:
                    v_gt = convert_value(atom_variable[k][v_name])
                    if k not in prediction or v_name not in prediction[k]:
                        # print(v_pred)
                        flag_variables.append(0)
                    else:
                        v_pred = convert_value(prediction[k][v_name])
                        if not isinstance(v_pred, list):
                            v_pred = [v_pred]
                        v_gt = convert_value(v_gt)
                        if v_pred == v_gt:
                            flag_variables.append(1)
                        else:
                            if Ellipsis in v_pred:
                                if v_pred[0] == v_gt[0] and v_pred[-1] == v_gt[-1]:
                                    flag_variables.append(1)
                                else:
                                    flag_variables.append(0)
                            else:
                                flag_variables.append(0)
        ## then check iterables:
        for k in atom_iterable:
            for i_name in atom_iterable[k]:
                i_gt = convert_value(atom_iterable[k][i_name])
                if k not in prediction or i_name not in prediction[k]:
                    flag_iterables.append(0)
                else:
                    i_pred = convert_value(prediction[k][i_name])
                    if not isinstance(i_pred, list):
                        i_pred = [i_pred]
                    i_gt = convert_value(i_gt)
                    # print(i_gt)
                    if i_pred == i_gt:
                        flag_iterables.append(1)
                    elif len(i_gt) > 0 and isinstance(i_gt[0], list):
                        if i_pred == i_gt[0]:
                            flag_iterables.append(1)
                        elif Ellipsis in i_pred:
                            if i_pred[0] == i_gt[0][0] and i_pred[-1] == i_gt[0][-1]:
                                flag_iterables.append(1)
                            else:
                                flag_iterables.append(0)
                    elif len(i_gt)==0:
                        if i_pred:
                            flag_iterables.append(1)
                        else:
                            flag_iterables.append(1)
                    ## pred returns a string
                    else:
                        try:
                            ## todo: pred returns string
                            if Ellipsis in i_pred:
                                if i_pred[0] == i_gt[0] and i_pred[-1] == i_gt[-1]:
                                    flag_iterables.append(1)
                                else:
                                    flag_iterables.append(0)
                            else:
                                flag_iterables.append(0)
                        except:
                            flag_iterables.append(0)
        label_iterables = 0 if 0 in flag_iterables else 1
        label_variables = 0 if 0 in flag_variables else 1
        labels[k] = [label_variables, label_iterables]
    return labels

def compare_prediction_condition(prediction, gt_conditon, gt_branches):
    labels = {}
    for atom_condition, atom_branch in zip(gt_conditon, gt_branches):
        flag_conditions, flag_branches = [], []
        ## first process conditions
        for k in atom_condition:
            for c_name in atom_condition[k]:
                c_gt = convert_value(atom_condition[k][c_name])
                c_name_pred = f"({c_name})"
                if k not in prediction or c_name_pred not in prediction[k]:
                    flag_conditions.append(0)
                else:
                    c_pred = convert_value(prediction[k][c_name_pred])
                    if isinstance(c_pred, list):
                        if c_pred == c_gt:
                            flag_conditions.append(1)
                        else:
                            flag_conditions.append(0)
                    else:
                        if [c_pred] == c_gt:
                            flag_conditions.append(1)
                        else:
                            flag_conditions.append(0)
        ## Then branches
        for k in atom_branch:
            b_gt = convert_value(atom_branch[k]['taken'])
            if k not in prediction or 'taken' not in prediction[k]:
                flag_branches.append(0)
            else:
                b_pred = prediction[k]['taken'].replace("Y", '"Y"').replace("N", '"N"')
                b_pred = convert_value(b_pred)
                if isinstance(b_pred, list):
                    if b_pred == b_gt:
                        flag_branches.append(1)
                    else:
                        flag_branches.append(0)
                else:
                    if [b_pred] == b_gt:
                        flag_branches.append(1)
                    else:
                        flag_branches.append(0)
        label_condition = 0 if 0 in flag_conditions else 1
        label_branch = 0 if 0 in flag_branches else 1
        labels[k] = [label_condition, label_branch]
    return labels
                 
                
                    
                    


if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default='none')
    parser.add_argument("--dataset", type=str, default='none', help="select one from [humaneval, HumanEvalFix]")
    
    args = parser.parse_args()
    model = args.model
    dataset = args.dataset
    
    path_branch_condition = f"./dataset/summary/{dataset}_condition_branch.json"
    dataset_root = f"./dataset/{dataset}"
    branch_condition_mapping = json.load(open(path_branch_condition, 'r'))
    loop_data = read_loop_data(dataset)
    condition_data = read_condition_data(dataset)
    branch_data = read_branch_data(dataset)

    summary_dir = "./Experiment_Results/summary"
    os.makedirs(summary_dir, exist_ok=True)
    write_path = f"{summary_dir}/{model.split('/')[-1]}_{dataset}.json"
    
    summary = {}
    for program_id in os.listdir(dataset_root):
        # print(program_id)
        py_path = f"./Experiment_Results/{model}/{dataset}/{program_id}/variable.txt"
        pred_output_path = f"./Experiment_Results/{model}/{dataset}/{program_id}/predict.txt"
        gt_output_path = f"{dataset_root}/{program_id}/output.txt"
        py_file_path = f"{dataset_root}/{program_id}/main.py"
        
        if not os.path.exists(pred_output_path):
            # print(pred_output_path)
            continue
        else:
            # print(pred_output_path)
            pass
        pred_output = open(pred_output_path, 'r').read().lstrip().strip('\n')
        gt_output = open(gt_output_path, 'r').read().lstrip().strip('\n')
        pred_output = convert_value(pred_output)
        gt_output = convert_value(gt_output)
        if pred_output == gt_output:
            l_o = 1
        else:
            l_o = 0
        
        res = parse_comments(py_path)
        gt_iterable, gt_variable = get_loop_gt(program_id, loop_data)
        # print(gt_iterable)
        gt_conditions, gt_branches = get_condition_branch_gt(program_id, branch_data, condition_data, branch_condition_mapping)
        
        if gt_iterable:
            l1 = compare_predict_loop(res, gt_variable, gt_iterable)
        else:
            l1 = {}
        if gt_conditions:
            l2 = compare_prediction_condition(res, gt_conditions, gt_branches)
        else:
            l2 = {}
        
        overall_results = {
            "type": "",
            "labels": [],
            "reasoning": 1,
            "output": l_o
        }
        
        overall_results["type"] = get_type(py_file_path)
        for lo in l1:
            # print(l1[lo])
            label_concat = l1[lo].copy()
            label_concat.append(l_o)
            if label_concat in [[1,1,1], [0,0,0], [1,0,0], [0,1,0], [1,1,0]]:
                overall_results["labels"].append({
                    "lino": lo,
                    "type": "loop",
                    "label": label_concat,
                    "reasoning": 1
                })
            else:
                overall_results["labels"].append({
                    "lino": lo,
                    "type": "loop",
                    "label": label_concat,
                    "reasoning": 0
                })            
        
        for lo in l2:
            label_concat = l2[lo].copy()
            label_concat.append(l_o)
            if label_concat in [[1,1,1], [0,0,0], [1,0,0], [1,1,0]]:
                overall_results["labels"].append({
                    "lino": lo,
                    "type": "condition",
                    "label": label_concat,
                    "reasoning": 1
                })
            else:
                overall_results["labels"].append({
                    "lino": lo,
                    "type": "condition",
                    "label": label_concat,
                    "reasoning": 0
                })
        reasoning_labels = [i['reasoning'] for i in overall_results['labels']]
        if 0 in reasoning_labels:
            overall_results['reasoning'] = 0
        summary[program_id] = overall_results
        # print(overall_results)
    if not os.path.exists(write_path):
        with open(write_path, 'w') as wr:
            json.dump(summary, wr, indent=4)
        
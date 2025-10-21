import json
import os
import argparse

def loc_incorrect_failure(model, dataset):
    results = {}
    json_path = f"./Experiment_Results/summary/{model}_{dataset}.json"
    
    
    wr_folder = "./Experiment_Results/summary/incorrect_output"
    if not os.path.exists(wr_folder):
        os.makedirs(wr_folder)

    wr_path = f"{wr_folder}/{model}_{dataset}.json"

    summary = json.load(open(json_path, 'r'))
    for problem_id in summary:
        data = summary[problem_id]
        if data['type'] == 'Other':
            continue
        if data['output'] == 1:
            continue
        constructs = data["labels"]
        ## sort constructs using lineno
        constructs = sorted(constructs, key=lambda cons:cons['lino'])
        ## by default: [1,1,1]
        if data['type'] == "LO":
            wrong_label = [1,1,'X','X',0]
        elif data['type'] == "CO":
            wrong_label = ['X','X',1,1,0]
        else:
            wrong_label = [1, 1, 1, 1, 0]
        
        for construct in constructs:
            if construct['label'][0] == 0 or construct['label'][1] == 0:
                if construct['type'] == "loop":
                    wrong_label = construct['label'].copy()
                    wrong_label.insert(2, 'X')
                    wrong_label.insert(3, 'X')
                    break
                elif construct['type'] == 'condition':
                    wrong_label = construct['label'].copy()
                    wrong_label.insert(0, 'X')
                    wrong_label.insert(1, 'X')
                    break
        results[problem_id] = {
            "type":data['type'],
            "label": wrong_label
        }
        
    with open(wr_path, 'w') as wr:
        json.dump(results, wr, indent=4)

def count_failure(model, dataset):
    json_path = f"./Experiment_Results/summary/incorrect_output/{model}_{dataset}.json"
    data = json.load(open(json_path, 'r'))
    summary = {
        "LO":{},
        "CO":{},
        "LC":{}
    }
    for d in data:
        label = "_".join([str(t) for t in data[d]['label']])
        if label not in summary[data[d]["type"]]:
            summary[data[d]["type"]][label] = 0
        summary[data[d]["type"]][label] += 1
    ## PRETTY PRINT
    print("V_l, I_l, P_c, B_c")
    for k in summary:
        print(f"======{k}======")
        for j in summary[k]:
            if k == "LO":
                if j == "0_1_X_X_0":
                    j_print = "0_1_X_X"
                    print(f"{j_print}: {summary[k][j]}")
                elif j == "1_0_X_X_0":
                    j_print = "1_0_X_X"
                    print(f"{j_print}: {summary[k][j]}")
                elif j == "0_0_X_X_0":
                    j_print = "0_0_X_X"
                    print(f"{j_print}: {summary[k][j]}")
            elif k == "CO":
                if j == "X_X_0_0_0":
                    j_print = "X_X_0_0"
                    print(f"{j_print}: {summary[k][j]}")
            elif k == "LC":
                if j == "0_1_X_X_0":
                    j_print = "0_1_X_X"
                    print(f"{j_print}: {summary[k][j]}")
                elif j == "1_0_X_X_0":
                    j_print = "1_0_X_X"
                    print(f"{j_print}: {summary[k][j]}")
                elif j == "0_0_X_X_0":
                    j_print = "0_0_X_X"
                    print(f"{j_print}: {summary[k][j]}")
                elif j == "X_X_0_0_0":
                    j_print = "X_X_0_0"
                    print(f"{j_print}: {summary[k][j]}")


def loc_sus_output(model):
    results = {}
    json_path = f"/home/changshu/CODEMIND/Experiment_Results/adaptive_loop_condition_branch/summary/new/{model}_humaneval.json"
    wr_path = f"/home/changshu/CODEMIND/Experiment_Results/adaptive_loop_condition_branch/summary/sus_output/{model}_humaneval.json"
    
    summary = json.load(open(json_path, 'r'))
    for problem_id in summary:
        data = summary[problem_id]
        if data['type'] == 'Other':
            continue
        if data['output'] == 0 or data['reasoning']==1:
            continue
        constructs = data["labels"]
        ## sort constructs using lineno
        constructs = sorted(constructs, key=lambda cons:cons['lino'])
        ## by default: [1,1,1]
        # if data['type'] == "LO":
        #     wrong_label = [1,1,'X','X',0]
        # elif data['type'] == "CO":
        #     wrong_label = ['X','X',1,1,0]
        # else:
        #     wrong_label = [1, 1, 1, 1, 0]
        
        for construct in constructs:
            if construct['label'][0] == 0 or construct['label'][1] == 0:
                if construct['type'] == "loop":
                    wrong_label = construct['label'].copy()
                    wrong_label.insert(2, 'X')
                    wrong_label.insert(3, 'X')
                    break
                elif construct['type'] == 'condition':
                    wrong_label = construct['label'].copy()
                    wrong_label.insert(0, 'X')
                    wrong_label.insert(1, 'X')
                    break
        results[problem_id] = {
            "type":data['type'],
            "label": wrong_label
        }
    # print(results)
    with open(wr_path, 'w') as wr:
        json.dump(results, wr, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default='none')
    parser.add_argument("--dataset", type=str, default='none')
    args = parser.parse_args()
    model = args.model
    dataset = args.dataset
    
    loc_incorrect_failure(model, dataset)
    count_failure(model, dataset)
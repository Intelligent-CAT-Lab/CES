import json
import os
import argparse
def load_task_label(model, task, dataset):
    path_br = f"./Experiment_Results/summary/{task}/{model}_{dataset}.json"
    task_labels = json.load(open(path_br, 'r'))
    return task_labels

def load_ces_labels(model, dataset):
    path_ces = f"./Experiment_Results/summary/{model}_{dataset}.json"
    ces_labels = json.load(open(path_ces, 'r'))
    return ces_labels

def load_bug_locations(dataset):
    path_locations = f"./dataset/summary/{dataset}_bug_loc.json"
    bug_locations = json.load(open(path_locations, 'r'))
    return bug_locations

def find_explainability(model, task, dataset):
    print(model, task)
    labels_task = load_task_label(model, task, dataset)
    labels_ces = load_ces_labels(model, dataset)
    bug_locs = load_bug_locations(dataset)
    
    correct_reasoning = []
    sus_reasoning = []
    less_sus_reasoning = []
    invalid_reasoning = []
    for key in labels_task:
        if labels_task[key] == 1:
            ## if the M succeed on the task
            ## check its reasoning
            if key not in labels_ces: continue
            flg = 1
            reasoning_failures = []
            for l in labels_ces[key]['labels']:
                if l ['label'] != [1,1,1]:
                    reasoning_failures.append(l)
            if labels_ces[key]['reasoning'] == 1 and labels_ces[key]['output'] ==1:
                if len(labels_ces[key]['labels']) == 0:
                   less_sus_reasoning.append(key)
                else:
                    correct_reasoning.append(key)
            elif labels_ces[key]['reasoning'] == 0:
                invalid_reasoning.append(key)
            else:
                if len(reasoning_failures) == 0:
                    less_sus_reasoning.append(key)
                else:
                    reasoning_failure_loc = reasoning_failures[0]['lino']
                    bug_loc = bug_locs[key][0]
                    if reasoning_failure_loc+1  < bug_loc:
                        sus_reasoning.append(key)
                    else:
                        less_sus_reasoning.append(key)

    summary = {
        'correct': correct_reasoning,
        'sus_reasoning': sus_reasoning,
        'less_sus_reasoning': less_sus_reasoning,
        'invalid_reasoning': invalid_reasoning
    }
    
    print("confident success:", len(correct_reasoning))
    print("suspicious success:", len(sus_reasoning))
    print("likely success:", len(less_sus_reasoning))
    print("incoherent:", len(invalid_reasoning))
    wr_folder = "./Experiment_Results/summary/bug_task_analysis"
    if not os.path.exists(wr_folder):
        os.makedirs(wr_folder)
    wr_path = f"{wr_folder}/{model}_{task}.json"
    with open(wr_path, 'w') as wr:
        json.dump(summary, wr, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default='none')
    parser.add_argument("--dataset", type=str, default='none', help="select one from [CodeNet, Avatar, cruxeval, mbpp, humaneval]")
    args = parser.parse_args()
    model = args.model
    dataset = args.dataset
    for task in ["BR", "BP", "BL"]:
        if task == "BR":
            print(f"======Bug Repair {model}  {dataset} ======")
        if task == "BL":
            print(f"======Bug Localization  {model}  {dataset} ======")
        if task == "BP":
            print(f"======Bug Prediction  {model}  {dataset} ======")
        find_explainability(model, task, dataset)

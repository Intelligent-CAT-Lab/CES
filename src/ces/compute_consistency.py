import json
from collect_prime_path import extract_prime_path
import argparse
def main_analysis_path_bk(model):
    json_path = f"/home/changshu/CODEMIND/Experiment_Results/adaptive_loop_condition_branch/summary/{model}_humaneval.json"
    json_data = json.load(open(json_path, 'r'))
    coverage_data = extract_prime_path()
    cleaned_results = {}
    for d in json_data:
        k = d.split("__")[0]
        if k not in cleaned_results:
            cleaned_results[k] = {
                'label':[],
                'coverage': []
            }
        cleaned_results[k]['label'].append(json_data[d]['label_1'])
        cleaned_results[k]['coverage'].append(coverage_data[d])
    
    strong_reasoning, weak_reasoning = 0, 0
    for k in cleaned_results:
        if len(set(cleaned_results[k]['coverage'])) == 1:
            continue
        if cleaned_results[k]['label'] == ['1_0_0_0', '1_0_0_0', "1_0_0_0"]:
            if len(set(cleaned_results[k]['coverage'])) > 1:
                strong_reasoning += 1
                print(k)
            if len(set(cleaned_results[k]['coverage'])) == 1:
                weak_reasoning += 1
        else:
            # print(cleaned_results[k]['label'])
            if len(set(cleaned_results[k]['coverage'])) > 1:
                weak_reasoning += 1
    random_reasoning = 164 - strong_reasoning - weak_reasoning
                
    print(strong_reasoning, weak_reasoning, random_reasoning)
    
def main_analysis_path(model):
    json_path = f"./Experiment_Results/summary/{model}_humaneval.json"
    json_data = json.load(open(json_path, 'r'))
    coverage_data = extract_prime_path()
    cleaned_results = {}
    for d in json_data:
        k = d.split("__")[0]
        if k not in cleaned_results:
            cleaned_results[k] = {
                'label':[],
                'coverage': []
            }
        if json_data[d]["reasoning"] == 1 and json_data[d]["output"] == 1:
            cleaned_results[k]['label'].append(1)
        else:
            cleaned_results[k]['label'].append(0)
        cleaned_results[k]['coverage'].append(coverage_data[d])
    
    strong_reasoning, weak_reasoning = 0, 0
    for k in cleaned_results:
        if len(set(cleaned_results[k]['coverage'])) == 1:
            continue
        if cleaned_results[k]['label'] == [1, 1, 1]:
            if len(set(cleaned_results[k]['coverage'])) > 1:
                strong_reasoning += 1
            if len(set(cleaned_results[k]['coverage'])) == 1:
                weak_reasoning += 1
        else:
            # print(cleaned_results[k]['label'])
            if len(set(cleaned_results[k]['coverage'])) > 1:
                weak_reasoning += 1
    random_reasoning = 164 - strong_reasoning - weak_reasoning
                
    print(strong_reasoning, weak_reasoning, random_reasoning)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default='none')
    args = parser.parse_args()
    model = args.model
    main_analysis_path(model)
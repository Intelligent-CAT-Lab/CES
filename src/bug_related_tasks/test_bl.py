import os
import json
import argparse
def cleanup(result_root):
    for d in os.listdir(result_root):
        path_bl = os.path.join(result_root, d, 'response.txt')
        if not os.path.exists(path_bl):
            continue
        text = open(path_bl, 'r').read()
        if "Magicoder" in result_root:
            try:
                response = text.split("```response")[1].split("```")[0].strip().strip("\n")
            except:
                pass
        elif "semcoder" in result_root:
            response = text.split("```response")[-1].split("```")[0].strip().strip("\n")
        else:
            try:
                response = text.split("```response")[-1].split("```")[0].strip().strip("\n")
            except:
                response = "err"
        wr_path = path_bl.replace("response", "predict")
        with open(wr_path, 'w') as wr:
            wr.write(response)

def check_output(result_root, dataset):
    model_name = result_root.split("/")[-2]
    wr_folder = "./Experiment_Results/summary/BL"
    if not os.path.exists(wr_folder):
        os.makedirs(wr_folder)
    wr_path = f"{wr_folder}/{model_name}_{dataset}.json"
    results = {}
    dataset_root = f"./dataset/{dataset}"
    correct, total = 0,0
    for d in os.listdir(result_root):
        total += 1
        hf_id = d
        path_bl = os.path.join(result_root, d, 'predict.txt')
        path_gt = os.path.join(dataset_root, hf_id, 'buggy_line.txt')
        pred = open(path_bl, 'r').read().strip('\n').strip().replace(" ",'')
        gt = open(path_gt, 'r').read().strip('\n').strip().replace(" ",'')
        if pred == gt:
            correct += 1
            results[d] = 1
        else:
            results[d] = 0
            
    print(correct, total, correct/total)
    with open(wr_path, 'w') as wr:
        json.dump(results, wr, indent=4)        
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default='none')
    parser.add_argument("--dataset", type=str, default='none', help="select one from [HumanEvalFix]")
    args = parser.parse_args()

    model_id = args.model
    dataset = args.dataset    
    result_root = f"./Experiment_Results/BL/{model_id}/{dataset}"

    cleanup(result_root)
    check_output(result_root, dataset)
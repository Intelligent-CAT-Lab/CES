import os
import json
import argparse
def cleanup(result_root):
    for d in os.listdir(result_root):
        path_bug = os.path.join(result_root, d, 'response.txt')
        
        
        if not os.path.exists(path_bug):
            continue
        text = open(path_bug, 'r').read()
        if "Magicoder" in result_root:
            try:
                response = text.split("```response")[1].split("```")[0].strip().strip("\n")
            except:
                pass
        elif "semcoder" in result_root:
            try:
                response = text.split("```response")[1].split("```")[0].strip().strip("\n")
            except:
                pass
        else:
            if "```response" in text:
                response = text.split("```response")[1].split("```")[0].strip().strip("\n")
            else:
                response = "err"
        wr_path = path_bug.replace("response", "predict")
        with open(wr_path, 'w') as wr:
            wr.write(response)

def check_output(result_root, dataset):
    model_name = result_root.split("/")[-2]
    
    wr_folder = "./Experiment_Results/summary/BP"
    if not os.path.exists(wr_folder):
        os.makedirs(wr_folder)
    wr_path = f"{wr_folder}/{model_name}_{dataset}.json"
    results = {}
    correct, total = 0,0
    for d in os.listdir(result_root):
        total += 1
        path_bug = os.path.join(result_root, d, 'predict.txt')
        if not os.path.exists(path_bug):
            continue
        pred_buggy = open(path_bug, 'r').read()
        if "Yes" in pred_buggy:
            correct += 1
            results[d] = 1
        else:
            results[d] = 0
    with open(wr_path, 'w') as wr:
        json.dump(results, wr, indent=4)
    print(correct, total, correct/total)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default='none')
    parser.add_argument("--dataset", type=str, default='none', help="select one from [HumanEvalFix]")
    args = parser.parse_args()

    model_id = args.model
    dataset = args.dataset    
    result_root = f"./Experiment_Results/BP/{model_id}/{dataset}"

    cleanup(result_root)
    check_output(result_root, dataset)
import os
import json
import argparse

def pprint(model, dataset):
    summary_path = f"./Experiment_Results/summary/{model.split('/')[-1]}_{dataset}.json"
    summary = json.load(open(summary_path, 'r'))
    
    statistics = {
        'LC':{},
        'LO':{},
        "CO":{},
        "Other":{},
        "Overall":{}
    }
    
    for key in summary:
        label = str(f"{summary[key]['reasoning']}{summary[key]['output']}")
        if label not in statistics[summary[key]['type']]:
            statistics[summary[key]['type']][label] = 0
        statistics[summary[key]['type']][label] += 1
        if label not in statistics["Overall"]:
            statistics["Overall"][label] = 0
        statistics["Overall"][label] += 1
    
    s1 = sum([statistics["CO"][t] for t in statistics["CO"]])
    print("="*6, "CO", "="*6)
    print("(Coherent Reasoning, Correct Output),   Ratio")
    for k in statistics["CO"]:
        print(k, statistics["CO"][k]/s1)
    s2 = sum([statistics["LO"][t] for t in statistics["LO"]])
    print("="*6, "LO", "="*6)
    print("(Coherent Reasoning, Correct Output),   Ratio")
    for k in statistics["LO"]:
        print(k, statistics["LO"][k]/s2)
    s3 = sum([statistics["LC"][t] for t in statistics["LC"]])
    print("="*6, "LC", "="*6)
    print("(Coherent Reasoning, Correct Output),   Ratio")
    for k in statistics["LC"]:
        print(k, statistics["LC"][k]/s3)    
    s4 = sum([statistics["Other"][t] for t in statistics["Other"]])
    print("="*6,"Other", "="*6)
    print("(Coherent Reasoning, Correct Output),   Ratio")
    for k in statistics["Other"]:
        print(k, statistics["Other"][k]/(53*3))      
    s5 = sum([statistics["Overall"][t] for t in statistics["Overall"]])
    print("="*6,"Overall", "="*6)
    print("(Coherent Reasoning, Correct Output),   Ratio")
    for k in statistics["Overall"]:
        print(k, statistics["Overall"][k]/(164*3))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default='none')
    parser.add_argument("--dataset", type=str, default='none')
    args = parser.parse_args()
    model_id = args.model          
    dataset = args.dataset
    pprint(model_id,dataset)
        
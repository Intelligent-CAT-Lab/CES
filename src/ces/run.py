import os
import json
from create_prompts import create_prompt
from transformers import AutoModelForCausalLM, AutoTokenizer
from prompts import chatgpt_generator, huggingface_generator, huggingface_generator_chat, generator_gemini, generator_lllm, generator_vllm
from tqdm import tqdm
import argparse

AUTH_TOKEN = os.getenv('AUTH_TOKEN')
MAX_NEW_TOKEN = 2048
def read_loop_data(dataset):
    root = "dataset/summary"
    
    iterator_path_orig = os.path.join(root, f"{dataset}_iterator.json")
    condition_path_orig = os.path.join(root, f"{dataset}_control.json")
    iterator_data_orig = json.load(open(iterator_path_orig, 'r'))
    control_data_orig = json.load(open(condition_path_orig, 'r'))

    cleaned_data = {}
    for k in control_data_orig.keys():
        cleaned_data[k] = {
            'iterator':{},
            'control':{},
            'all':{}
        }
        
        if k in iterator_data_orig:
            ## append iterators for FOR loops
            for i in iterator_data_orig[k]['For']:
                lineno = i['line_no']
                iterators = i["iterator"]
                iterator_gts = i["iterator_gt"]
                cleaned_data[k]['iterator'][lineno] = {}
                cleaned_data[k]['all'][lineno] = {}
                for ite, ite_gt in zip(iterators, iterator_gts):
                    cleaned_data[k]['iterator'][lineno][ite] = ite_gt
                    cleaned_data[k]['all'][lineno][ite] = ite_gt
        ## append loop control
        for j in control_data_orig[k]:
            line_no = j["line_no"] - 1
            conditions = j['condition']
            condition_gts = j['condition_gt']
            cleaned_data[k]['control'][line_no] = {}
            if line_no not in cleaned_data[k]['all'].keys():
                cleaned_data[k]['all'][line_no] = {}
            if condition_gts:
                for cond, cond_gt in zip(conditions, condition_gts):
                    cleaned_data[k]['control'][line_no][cond] = cond_gt
                    cleaned_data[k]['all'][line_no][cond] = cond_gt
            else:
                for cond in conditions:
                    cleaned_data[k]['control'][line_no][cond] = []
                    cleaned_data[k]['all'][line_no][cond] = []             
    return cleaned_data


def read_condition_data(dataset):
    root = "dataset/summary"
    condition_path = os.path.join(root, f"{dataset}_condition.json")
    condition_data = json.load(open(condition_path, 'r'))
    cleaned_data = {}
    for k in condition_data:
        cleaned_data[k]={'all':{}}
        if condition_data[k]:
            for item in condition_data[k]:
                line_no = item['line_no']
                conditions = item['condition']
                values = item['condition_gt']
                cleaned_data[k]['all'][line_no] = {}
                for condition, value in zip(conditions, values):
                    # if len(value) < 100:
                    cleaned_data[k]['all'][line_no][condition]=value
    return cleaned_data

def read_branch_data(dataset):
    root = "dataset/summary"
    branch_path = os.path.join(root, f"{dataset}_branch.json")
    branch_data = json.load(open(branch_path, 'r'))
    return branch_data


def find_path(dataset, pl):
    root = "dataset"
    
    data_path = os.path.join(root, dataset)
    if not os.path.exists(data_path):
        print(f"{data_path} not found")
    return data_path
            
def annotate_code(code_path, loop_data, condition_data, branch_data):
    annotated_lines = []
    comments = {}
    for k in loop_data.keys():
        new_text = " ## "
        for var in loop_data[k]:
            new_text += f"[STATE]{var}=??[/STATE]"
        comments[k] = new_text
    for k in condition_data:
        new_text = comments[k] if k in comments else " ## "
        for var in condition_data[k]:
            new_text += f"[CONDITION]({var})=??[/CONDITION]"
        comments[k] = new_text
    for k in branch_data:
        new_text = comments[int(k)] if int(k) in comments else " ## "
        new_text += f"[BRANCH]taken=??[/BRANCH]"
        comments[int(k)] = new_text
    with open(code_path, 'r') as file:
        for line_no, line in enumerate(file, start=0):
            if line_no in comments:
                new_line = line.rstrip('\n') + comments[line_no] + '\n'
                annotated_lines.append(new_line)
            else:
                annotated_lines.append(line)
    return ''.join(annotated_lines)

def load_model(model_id, cache_dir, api_type):
    ## openai models:
    if api_type != "vllm":
        return model_id, None
    ## huggingface models
    else:
        model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", cache_dir=cache_dir)
        tokenizer = AutoTokenizer.from_pretrained(model_id, device_map="auto", cache_dir=cache_dir)
        return model, tokenizer

def main(dataset, pl, model_id, cache_dir, write_dir, direct, no_nl):
    json_path = "config/model_config.json"
    model_config = json.load(open(json_path, 'r'))
    api_type = model_config[model_id]["api"]

    loop_data = read_loop_data(dataset)
    condition_data = read_condition_data(dataset)
    branch_data = read_branch_data(dataset)

    dataset_path = find_path(dataset, pl)
    model, tokenizer = load_model(model_id, cache_dir, api_type) 

    write_root = os.path.join(write_dir, model_id.split("/")[-1], dataset)
    if no_nl:
        write_root = os.path.join(write_dir,'no_nl', model_id.split("/")[-1], dataset)
    if direct:
        write_root = os.path.join(write_dir, 'direct', model_id.split("/")[-1], dataset)

    for d in tqdm(os.listdir(dataset_path)):
        meta_data_loop = loop_data[d]['all'] if d in loop_data.keys() else {}
        meta_data_condition = condition_data[d]['all'] if d in condition_data.keys() else {}
        meta_data_branch = branch_data[d] if d in branch_data.keys() else {}

        code_path = os.path.join(dataset_path, d, 'main.py')
        source_code = open(code_path, 'r').read()
        input_path = os.path.join(dataset_path, d , 'input.txt')
        
        new_code = annotate_code(code_path, meta_data_loop, meta_data_condition, meta_data_branch)
        
        code_input = open(input_path, 'r').read().strip('\n')

        write_folder = os.path.join(write_root, d)
        if not os.path.exists(write_folder):
            os.makedirs(write_folder)
        write_path = os.path.join(write_folder, 'response.txt')

        if direct:
            prompt = create_prompt(code_path, model_id, source_code, code_input, dataset, pl, direct, no_nl)
        else:
            if not meta_data_condition and not meta_data_loop:
                prompt = create_prompt(code_path, model_id, source_code, code_input, dataset, pl, True, no_nl)
            else:
                prompt = create_prompt(code_path, model_id, new_code, code_input, dataset, pl, direct, no_nl)
        
        
        
        if not prompt:
            print(f"skip {d}")
            continue
        if api_type == "huggingface":
            response = huggingface_generator((model, tokenizer), prompt, MAX_NEW_TOKEN)
        elif api_type == "openai":
            err_flg, response = chatgpt_generator(model_id, prompt)
            if err_flg:
                response = 'ERR: reaches maximum context length'
        elif api_type == "litellm":
            response = generator_lllm(model_id, prompt)
        elif api_type == "vllm":
            response = generator_vllm(model, prompt, MAX_NEW_TOKEN)   
        if response:
            with open(write_path, 'w') as wr:
                wr.write(response)
        else:
            print(f"{d} response empty")
        

        

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default='none')
    parser.add_argument("--dataset", type=str, default='none', help="select one from [humaneval, HumanEvalFix]")
    parser.add_argument("--cache", type=str, default="./cache")
    parser.add_argument("--writePath", type=str, default="./Experiment_Results")
    parser.add_argument("--pl", type=str, default="Python", help="select one from [Python, Java]")
    parser.add_argument("--direct", action="store_true")
    parser.add_argument("--no_nl", action="store_true")
    args = parser.parse_args()

    dataset = args.dataset
    pl = args.pl
    model_id = args.model 
    cache_dir = args.cache
    write_dir = args.writePath
    direct = args.direct
    no_nl = args.no_nl

    main(dataset, pl, model_id, cache_dir, write_dir, direct, no_nl)
    
    

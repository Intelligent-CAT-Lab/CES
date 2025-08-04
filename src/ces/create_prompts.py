from utils import parse_file
import os
import re

def load_instruction(model_id):
    if "CodeLlama" in model_id or "Mistral" in model_id:
        instructions = """You are given a piece of Python code and its output. You are asked to complete the following task:
1. First think step by step and explain the execution process of the code. Enclose your reasoning process between [REASONING] and [/REASONING].
2. Replace the "??" between [STATE] and [/STATE] in the comment with the state of a variable or the return value of a method call/expression.
3. Replace the "??" between [CONDITION] and [/CONDITION] in the comment with the the value of a predicate in the conditional statement.
4. Replace the "??" between [BRANCH] and [/BRANCH] in the comment with `Y` and `N`. If a branch is hit during the execution, then mark it with `Y`, otherwise mark it with `N`.
5. Enclose the annotated code with [PYTHON] AND [/PYTHON]
6. Finally print the output and enclose it with [OUTPUT] and [/OUTPUT].
"""
    else:
        instructions = """You are given a piece of Python code and its output. You are asked to complete the following task:
1. Replace the "??" between [STATE] and [/STATE] in the comment with the state of a variable or the return value of a method call/expression.
2. Replace the "??" between [CONDITION] and [/CONDITION] in the comment with the the value of a predicate in the conditional statement.
3. Replace the "??" between [BRANCH] and [/BRANCH] in the comment with `Y` and `N`. If a branch is hit during the execution, then mark it with `Y`, otherwise mark it with `N`.
4. Enclose the annotated code with [ANSWER] AND [/ANSWER]
5. Think step by step and print you reasoning process of the code execution.
6. Print the output and enclose it with [OUTPUT] and [/OUTPUT].
"""
    return instructions

question = """[QUESTION]
First print the step by step reasoning (wrapped with [REASONING] and [/REASONING]), then print the annotated code (wrapped with [PYTHON] and [PYTHON]), finally print the output (wrapped with [OUTPUT] and [OUTPUT]):
[/QUESTION]
"""
question_extended="""[QUESTION]
First print the step by step reasoning (wrapped with [REASONING] and [/REASONING]), then print the annotated code (wrapped with [PYTHON] and [PYTHON]), finally print the output (wrapped with [OUTPUT] and [OUTPUT]).
Replace all the '??' in comments with proper states/values/symbols.
[/QUESTION]
"""
def load_examples(model_id):
    if "CodeLlama-13b" in model_id or "CodeLlama-7b" in model_id:
        root = "./prompts_codellama"
    elif "Mistral" in model_id or "gpt-4-turbo" in model_id:
        root = "./prompts"
    else:
        root = "./prompts"
    
    path_if_in_nested_loop = os.path.join(root, "if_in_nested_loop.txt")
    path_if = os.path.join(root, "if.txt")
    path_else_if = os.path.join(root, "else_if.txt")
    path_nested_if = os.path.join(root, "nested_if.txt")
    path_for_loop = os.path.join(root, "for_loop.txt")
    path_while_loop = os.path.join(root, "while_loop.txt")
    path_nested_loop = os.path.join(root, "nested_loop.txt")
    path_if_in_for_loop = os.path.join(root, "if_in_for_loop.txt")
    path_if_outside_for_loop = os.path.join(root, "if_outside_for_loop.txt")
    path_if_in_while_loop = os.path.join(root, "if_in_while_loop.txt")
    path_if_outside_while_loop = os.path.join(root, "if_outside_while_loop.txt")
    path_simple = os.path.join(root, "simple.txt")
    
    text_if_in_nested_loop = open(path_if_in_nested_loop, 'r').read()
    text_if = open(path_if, 'r').read()
    text_else_if = open(path_else_if, 'r').read()
    text_nested_if = open(path_nested_if, 'r').read()
    text_for_loop = open(path_for_loop, 'r').read()
    text_while_loop = open(path_while_loop, 'r').read()
    text_nested_loop = open(path_nested_loop, 'r').read()
    text_if_in_for_loop = open(path_if_in_for_loop, 'r').read()
    text_if_outside_for_loop = open(path_if_outside_for_loop, 'r').read()
    text_if_in_while_loop = open(path_if_in_while_loop, 'r').read()
    text_if_outside_while_loop = open(path_if_outside_while_loop, 'r').read()
    text_simple = open(path_simple, 'r').read()
    
    
    

    prompts = {
        "if in nested_loop": text_if_in_nested_loop,
        "if": text_if,
        "else_if": text_else_if,
        "nested_if": text_nested_if,
        "for_loop": text_for_loop,
        "while_loop": text_while_loop,
        "nested_loop": text_nested_loop,
        "if in for_loop": text_if_in_for_loop,
        "else_if in for_loop": text_if_in_for_loop,
        "if outside while_loop": text_if_outside_while_loop,
        "nested_if outside while_loop": text_if_outside_while_loop,
        "if in while_loop": text_if_in_while_loop,
        "if outside for_loop": text_if_outside_for_loop,
        "nested_if in while_loop": text_if_in_while_loop,
        "nested_if in for_loop": text_if_in_for_loop,
        "nested_if in nested_loop": text_if_in_nested_loop,
        "simple": text_simple
    }
    return prompts
    

def select_examples(file_path, model_id):
    instruction = load_instruction(model_id)
    examples = load_examples(model_id)
    labels = parse_file(file_path)

    icl_examples= []
    for label in labels:
        if label not in examples:
            print(file_path)
            print(f"{label} not found")
            return False
        else:
            icl_examples.append(examples[label])
    
    if "CodeLlama-13b" in model_id or  "CodeLlama-7b" in model_id:
        prompt = "Bellow are some examples:\n\n" + '\n\n'.join(icl_examples)
    else:
        prompt = instruction + "\n" + '\n\n'.join(icl_examples)
    return prompt

def create_prompt_deepseekcoder(prompt, pl, dataset, direct, no_nl):
    prompt_role = "You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer."
    if pl == 'Python':
        if direct:
            prompt = prompt.replace('1. Replace the "??" between [STATE] and [/STATE] in the comment with the state of a variable or the return value of a method call/expression.\n', "")\
                .replace('2. Replace the "??" between [CONDITION] and [/CONDITION] in the comment with the the value of a predicate in the conditional statement.\n', "")\
                .replace('3. Replace the "??" between [BRANCH] and [/BRANCH] in the comment with `Y` and `N`. If a branch is hit during the execution, then mark it with `Y`, otherwise mark it with `N`.\n', "")\
                .replace('4. Enclose the annotated code with [ANSWER] AND [/ANSWER]\n', '')\
                .replace('5. Think step by step and print you reasoning process of the code execution.', '1. Think step by step and print you reasoning process of the code execution.')\
                .replace('6. Print the output and enclose it with [OUTPUT] and [/OUTPUT].', '2. Print the output and enclose it with [OUTPUT] and [/OUTPUT].')
            
            pattern = r"\[ANSWER](.*?)\[/ANSWER]"
            matches = re.findall(pattern, prompt, re.DOTALL)
            for match in matches:
                string_del = f"[ANSWER]{match}[/ANSWER]\n"
                prompt = prompt.replace(string_del, '')
        elif no_nl:
            prompt = prompt.replace("5. Think step by step and print you reasoning process of the code execution.\n", '')\
                .replace("6. Print the output and enclose it with [OUTPUT] and [/OUTPUT]", "5. Print the output and enclose it with [OUTPUT] and [/OUTPUT]")
            ## remove content between [REASONING] and [/REASONING]
            pattern = r"\[REASONING](.*?)\[/REASONING]"
            matches = re.findall(pattern, prompt, re.DOTALL)
            for match in matches:
                string_del = f"[REASONING]{match}[/REASONING]\n"
                prompt = prompt.replace(string_del, '')
        # else:
        if dataset in ['humaneval']:
            prompt = prompt_role + '\n' + '### Instruction\n' + prompt + "\n### Response"
    return prompt

def create_prompt_magicoder(prompt, pl, dataset, direct, no_nl):
    prompt_role = "You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions."
    if pl == 'Python':
        if direct:
            prompt = prompt.replace('1. Replace the "??" between [STATE] and [/STATE] in the comment with the state of a variable or the return value of a method call/expression.\n', "")\
                .replace('2. Replace the "??" between [CONDITION] and [/CONDITION] in the comment with the the value of a predicate in the conditional statement.\n', "")\
                .replace('3. Replace the "??" between [BRANCH] and [/BRANCH] in the comment with `Y` and `N`. If a branch is hit during the execution, then mark it with `Y`, otherwise mark it with `N`.\n', "")\
                .replace('4. Enclose the annotated code with [ANSWER] AND [/ANSWER]\n', '')\
                .replace('5. Think step by step and print you reasoning process of the code execution.', '1. Think step by step and print you reasoning process of the code execution.')\
                .replace('6. Print the output and enclose it with [OUTPUT] and [/OUTPUT].', '2. Print the output and enclose it with [OUTPUT] and [/OUTPUT].')
            
            pattern = r"\[ANSWER](.*?)\[/ANSWER]"
            matches = re.findall(pattern, prompt, re.DOTALL)
            for match in matches:
                string_del = f"[ANSWER]{match}[/ANSWER]\n"
                prompt = prompt.replace(string_del, '')           
        elif no_nl:
            prompt = prompt.replace("5. Think step by step and print you reasoning process of the code execution.\n", '')\
                .replace("6. Print the output and enclose it with [OUTPUT] and [/OUTPUT]", "5. Print the output and enclose it with [OUTPUT] and [/OUTPUT]")
            ## remove content between [REASONING] and [/REASONING]
            pattern = r"\[REASONING](.*?)\[/REASONING]"
            matches = re.findall(pattern, prompt, re.DOTALL)
            for match in matches:
                string_del = f"[REASONING]{match}[/REASONING]\n"
                prompt = prompt.replace(string_del, '')            
        if dataset in ['humaneval']:
            prompt = prompt_role + '\n' + '@@ Instruction\n' + prompt + "\n@@ Response"
    return prompt

def create_prompt_starcoder2(prompt, pl, dataset, direct, no_nl):
    if pl == 'Python':
        if direct:
            prompt = prompt.replace('1. Replace the "??" between [STATE] and [/STATE] in the comment with the state of a variable or the return value of a method call/expression.\n', "")\
                .replace('2. Replace the "??" between [CONDITION] and [/CONDITION] in the comment with the the value of a predicate in the conditional statement.\n', "")\
                .replace('3. Replace the "??" between [BRANCH] and [/BRANCH] in the comment with `Y` and `N`. If a branch is hit during the execution, then mark it with `Y`, otherwise mark it with `N`.\n', "")\
                .replace('4. Enclose the annotated code with [ANSWER] AND [/ANSWER]\n', '')\
                .replace('5. Think step by step and print you reasoning process of the code execution.', '1. Think step by step and print you reasoning process of the code execution.')\
                .replace('6. Print the output and enclose it with [OUTPUT] and [/OUTPUT].', '2. Print the output and enclose it with [OUTPUT] and [/OUTPUT].')
            
            pattern = r"\[ANSWER](.*?)\[/ANSWER]"
            matches = re.findall(pattern, prompt, re.DOTALL)
            for match in matches:
                string_del = f"[ANSWER]{match}[/ANSWER]\n"
                prompt = prompt.replace(string_del, '')
        elif no_nl:
            prompt = prompt.replace("5. Think step by step and print you reasoning process of the code execution.\n", '')\
                .replace("6. Print the output and enclose it with [OUTPUT] and [/OUTPUT]", "5. Print the output and enclose it with [OUTPUT] and [/OUTPUT]")
            ## remove content between [REASONING] and [/REASONING]
            pattern = r"\[REASONING](.*?)\[/REASONING]"
            matches = re.findall(pattern, prompt, re.DOTALL)
            for match in matches:
                string_del = f"[REASONING]{match}[/REASONING]\n"
                prompt = prompt.replace(string_del, '')
        if dataset in ['humaneval']:
            prompt = '<fim_prefix>' + prompt + "\n<fim_suffix><fim_middle>\n"
    return prompt


def create_prompt_codellama(prompt, pl, dataset, direct, no_nl):
    inst = load_instruction("CodeLlama-13b")
    prompt_role = f"<<SYS>>{inst}<</SYS>>"
    if pl == 'Python':
        if direct:
            inst = """You are given a piece of Python code and its output. You are asked to complete the following task:
1. First think step by step and explain the execution process of the code. Enclose your reasoning process between [REASONING] and [/REASONING].
2. Finally print the output and enclose it with [OUTPUT] and [/OUTPUT].
            """
            prompt_role =  f"<<SYS>>{inst}<</SYS>>"
            pattern = r"\[QUESTION](.*?)\[/QUESTION]"
            matches = re.findall(pattern, prompt, re.DOTALL)
            for match in matches:
                string_del = f"[QUESTION]{match}[/QUESTION]\n"
                prompt = prompt.replace(string_del, '')
            
            pattern = r"\[PYTHON](.*?)\[/PYTHON]"
            matches = re.findall(pattern, prompt, re.DOTALL)
            # print(matches)
            for match in matches:
                string_del = f"[PYTHON]{match}[/PYTHON]\n"
                prompt = prompt.replace(string_del, '')           
        elif no_nl:
            prompt_role = prompt_role.replace("1. First think step by step and explain the execution process of the code. Enclose your reasoning process between [REASONING] and [/REASONING].\n", '')\
                .replace('2. Replace the "??" between [STATE] and [/STATE]', '1. Replace the "??" between [STATE] and [/STATE]')\
                .replace('3. Replace the "??" between [CONDITION] and [/CONDITION]', '2. Replace the "??" between [CONDITION] and [/CONDITION]')\
                .replace('4. Replace the "??" between [BRANCH] and [/BRANCH]', '3. Replace the "??" between [BRANCH] and [/BRANCH]')\
                .replace('5. Enclose the annotated code with [PYTHON] AND [/PYTHON]', '4. Enclose the annotated code with [PYTHON] AND [/PYTHON]')\
                .replace('6. Finally print the output and enclose it with [OUTPUT] and [/OUTPUT].', '5. Finally print the output and enclose it with [OUTPUT] and [/OUTPUT].')
            pattern = r"\[REASONING](.*?)\[/REASONING]"
            matches = re.findall(pattern, prompt, re.DOTALL)
            for match in matches:
                string_del = f"[REASONING]{match}[/REASONING]\n"
                prompt = prompt.replace(string_del, '')
            
            pattern = r"\[QUESTION](.*?)\[/QUESTION]"
            matches = re.findall(pattern, prompt, re.DOTALL)
            for match in matches:
                string_del = f"[QUESTION]{match}[/QUESTION]\n"
                prompt = prompt.replace(string_del, '')            
        
        if dataset in ['humaneval']:
            prompt = "[INST]" + prompt_role + '\n' +  prompt  +"[/INST]"
    return prompt

def create_prompt_mistral(prompt, pl, dataset, direct):
    if pl == 'Python':
        if direct:
            pass
        else:
            if dataset in ['humaneval']:
                prompt = '[INST]' + prompt + "\n[/INST]"
    return prompt



def create_prompt(code_path, model_id, new_code, code_input, dataset, pl, direct, no_nl):
    icl_example = select_examples(code_path, model_id)
    if not icl_example:
        return False
    if "deepseek" in model_id:
        prompt = icl_example +  "\n\n[CODE]\n" + new_code + "[/CODE]\n\n" \
            + "[INPUT]\n" + code_input + "\n[/INPUT]\n"
        prompt = create_prompt_deepseekcoder(prompt, pl, dataset, direct, no_nl)
    elif "Magicoder" in model_id:
        prompt = icl_example +  "\n[CODE]\n" + new_code + "[/CODE]\n\n" \
            + "[INPUT]\n" + code_input + "\n[/INPUT]"
        prompt = create_prompt_magicoder(prompt, pl, dataset, direct, no_nl)
    elif "starcoder2-15b" in model_id:
        prompt = icl_example +  "\n[CODE]\n" + new_code + "[/CODE]\n\n" \
            + "[INPUT]\n" + code_input + "\n[/INPUT]"
        prompt = create_prompt_starcoder2(prompt, pl, dataset, direct, no_nl)
    elif "CodeLlama" in model_id or "CodeLlama-7b" in model_id:
        prompt = icl_example +  "\n[CODE]\n" + new_code + "[/CODE]\n\n" \
            + "[INPUT]\n" + code_input + "\n[/INPUT]\n\n" + question
        prompt = create_prompt_codellama(prompt, pl, dataset, direct, no_nl)
    elif "Mistral" in model_id:
        prompt = icl_example +  "\n[CODE]\n" + new_code + "[/CODE]\n\n" \
            + "[INPUT]\n" + code_input + "\n[/INPUT]\n\n" + question_extended
        prompt = create_prompt_mistral(prompt, pl, dataset, direct)
    elif "gpt-4-turbo" in model_id or "gemini" in model_id:
        prompt = icl_example +  "\n[CODE]\n" + new_code + "[/CODE]\n\n" \
            + "[INPUT]\n" + code_input + "\n[/INPUT]\n\n" + question_extended
            
    elif "semcoder" in model_id:
        prompt = icl_example +  "\n[CODE]\n" + new_code + "[/CODE]\n\n" \
            + "[INPUT]\n" + code_input + "\n[/INPUT]\n\n" + question_extended      
    return prompt


        
if __name__ == "__main__":
    code_path = "/home/changshu/CODEMIND/dataset/humaneval/HumanEval_47/main.py"
    model_id = "semcoder"
    new_code = """from typing import *
def longest(strings: List[str]) -> Optional[str]:
    if not strings: ## [CONDITION](not strings)=??[/CONDITION][BRANCH]taken=??[/BRANCH]
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings: ## [STATE]s=??[/STATE][STATE]strings=??[/STATE]
        if len(s) == maxlen: ## [CONDITION](len(s) == maxlen)=??[/CONDITION][BRANCH]taken=??[/BRANCH]
            return s
    """
    code_input = "longest(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) "
    dataset = "humaneval"
    pl = "Python"
    prompt = create_prompt(code_path, model_id, new_code, code_input, dataset, pl, False, True)

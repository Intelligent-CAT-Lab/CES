
icl_example = """
Fix bugs in has_close_elements.
Enclose the fixed code in ```python and ```. 

Buggy Code:
from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = elem - elem2
                if distance < threshold:
                    return True

    return False

Tests:
def check(has_close_elements):
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
    assert has_close_elements([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True
    assert has_close_elements([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False

check(has_close_elements)

The fixed code should satisfy the following natural language specification:
Write a Python function `has_close_elements(numbers: List[float], threshold: float) -> bool` to solve the following problem:
Check if in given list of numbers, are any two numbers closer to each other than
given threshold.

Fixed Code:
```python
from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False
```

"""

icl_example_cot = """
Fix bugs in below_zero.
First think step by step and simulate the execution of the provided test.
Enclose the fixed code in ```python and ```.

Buggy Code:
def below_zero(operations: List[int]) -> bool:
    balance = 0

    for op in operations:
        balance += op
        if balance == 0:
            return True

    return False

Tests:
assert below_zero([1, -2, 2, -2, 5, -5, 4, -4]) == True

The fixed code should satisfy the following natural language specification:
Write a Python function `below_zero(operations: List[int]) -> bool` to solve the following problem:
You're given a list of deposit and withdrawal operations on a bank account that starts with
zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
at that point function should return True. Otherwise it should return False.

Reasoning:
[Reasoning]
Now let's look at the program. The function initializes `balance` to 0. It iterates through each operation in the `operations` list, adjusting `balance` by adding each operation (`op`).
It checks if balance == 0 (which only detects when the balance exactly reaches zero, not when it goes below zero).
If balance == 0, the function returns True, though we're actually interested in whether balance < 0.
In the test case `operation` is initialized with [1, -2, 2, -2, 5, -5, 4, -4].
In the first iteration, `op`=1, `balance=1`.
In the second iteration, `op`=-2, `balance`=-1.
In the third iteration, `op`=2, `balance`=1.
In the forth iteration, `op`=-2, `balance`=-1.
In the fifth iteration, `op`=5, `balance`=4.
In the sixth iteration, `op`=-5, `balance`=-1. 
In the seventh iteration, `op`=4, `balance`=3. 
In the eighth iteration, `op`=-4, `balance`=-1. 
`balance` never exactly reaches zero at a point when it first goes negative and the function will return `False` as the output while the expected output is `True`.
However, if we were correctly checking `balance < 0`, the function would catch any negative balance.
[/Reasoning]

Fixed Code:
```python
def below_zero(operations: List[int]) -> bool:
    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False
```

"""
def create_prompt_magicoder(buggy, entry, tests, nl):
    if tests:
        test_info = f"Tests:\n{tests}"
    else:
        test_info = ""
    prompt = f'''You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions.
@@ Instruction
{icl_example_cot}
Fix bugs in {entry}.
First think step by step and simulate the execution of the provided test.
Enclose the fixed code in ```python and ```.

Buggy Code:
{buggy}

{test_info}

The fixed code should satisfy the following natural language specification:
{nl}
@@ Response
'''
    return prompt

def create_prompt_gpt_codeqwen(buggy, entry, tests, nl):
    if tests:
        test_info = f"Tests:\n{tests}"
    else:
        test_info = ""
    prompt=f'''
{icl_example_cot}
    
Fix bugs in {entry}.    
First think step by step and simulate the execution of the provided test.
Print the reasoning process. Enclose your reasoning process with "[Reasoning]" and "[/Reasoning]".
Enclose the fixed code in ```python and ```.

Buggy Code:
{buggy}

{test_info}

The fixed code should satisfy the following natural language specification:
{nl}

Reasoning:
'''
    return prompt

def create_prompt_codellama(buggy, entry, tests, nl):
    if tests:
        test_info = f"Tests:\n{tests}"
    else:
        test_info = ""
    prompt = f'''[INST]<<SYS>>
You are an expert Python programmer.
<</SYS>>
{icl_example_cot}

Fix bugs in {entry}. 
First think step by step and simulate the execution of the provided test.
Enclose the fixed code in ```python and ```.

Buggy Code:
{buggy}

{test_info}

The fixed code should satisfy the following natural language specification:
{nl}

Reasoning:
[/INST]
'''
    return prompt

def create_prompt_mistral(buggy, entry, tests, nl):
    if tests:
        test_info = f"Tests:\n{tests}"
    else:
        test_info = ""
    prompt = f'''[INST]Fix bugs in {entry}. 
Enclose the fixed code inside ```python and ```.

Buggy Code:
{buggy}

{test_info}

Reasoning:
[/INST]
'''
    return prompt

def create_prompt_deepseekcoder(buggy, entry, tests, nl):
    if tests:
        test_info = f"Tests:\n{tests}"
    else:
        test_info = ""
    prompt = f'''You are an expert Python programmer.Your task is to write a Python function to solve a programming problem.
### Instruction:
{icl_example_cot}

Fix bugs in {entry}. 
First think step by step and simulate the execution of the provided test.
Enclose the fixed code in ```python and ```.

Buggy Code:
{buggy}

{test_info}

The fixed code should satisfy the following natural language specification:
{nl}

Reasoning:
### Response:
'''
    return prompt

def create_prompt_starcoder(buggy, entry, tests):
    if tests:
        test_info = f"Tests:\n{tests}"
    else:
        test_info = ""
    prompt=f'''<fim_prefix>{icl_example_cot}
Fix bugs in {entry}.    
First think step by step and simulate the execution of the provided test.
Enclose the fixed code in ```python and ```.

Buggy Code:
{buggy}

{test_info}

The fixed code should satisfy the following natural language specification:
{nl}

Reasoning:
[Reasoning]
<fim_suffix><fim_middle>
'''
    return prompt

def create_prompt_wizardcoder(buggy, entry, tests):
    if tests:
        test_info = f"Tests:\n{tests}"
    else:
        test_info = ""
    prompt = f'''Below is an instruction that describes a task. Write a response that appropriately completes the request.
### Instruction:
Fix bugs in {entry}. 
Enclose the fixed code inside ```python and ```.

Buggy Code:
{buggy}

{test_info}
## Response:
'''
    return prompt

def create_prompt(model_id, buggy, nl, tests, sp):
    if "Magicoder" in model_id:
        prompt = create_prompt_magicoder(buggy, nl, tests, sp)
    if "gpt-4-turbo" in model_id or "gemini" in model_id or "semcoder" in model_id or "o4-mini-2025-04-16" in model_id or "deepseek-r1" in model_id:
        prompt = create_prompt_gpt_codeqwen(buggy, nl, tests, sp)
    if "CodeLlama" in model_id or "Llama-2" in model_id:
        prompt = create_prompt_codellama(buggy, nl, tests, sp)
    if "Mistral" in model_id:
        prompt = create_prompt_mistral(buggy, nl, tests)
    if "deepseek-coder" in model_id:
        prompt = create_prompt_deepseekcoder(buggy, nl, tests, sp)
    if "starcoder" in model_id:
        prompt = create_prompt_starcoder(buggy, nl, tests, sp)
    return prompt
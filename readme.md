# CES: Assessing Coherency and Consistency of Code Execution Reasoning by Large Language Models
Artifact for the paper Assessing Coherency and Consistency of Code Execution Reasoning by Large Language Models, accepted by  the 48th IEEE/ACM International Conference on Software Engineering (ICSE 2026).
Authors are Changshu Liu, Yang Chen, and Reyhaneh Jabbarvand.

## Getting Started
step 1. Run the following commands to install all the dependencies on your local machine:
```
conda create -n ces python=3.8
conda activate ces
pip install -r requirements.txt
```

Step 2. Go to `config/model_config.json` and edit the file with your OpenAI/Google AI Studio key.

Step 3. Install Python grammer for tree-sitter:
```
https://github.com/tree-sitter/tree-sitter-python.git
```
Step 4. Download the meta-data required by the experiments: [link](https://drive.google.com/file/d/1RjaS68WWYnWYhjlf1R6ITsHTXLSETWp5/view?usp=sharing). Unzip under `dataset`


Install Python grammer for tree-sitter:
```
https://github.com/tree-sitter/tree-sitter-python.git
```

Alternatively, we provide a Dockerfile to reproduce the results of CES.
Please download [Docker](https://www.docker.com/) and and then execute the following to create a docker image and execute the container in interactive mode:

```
docker build -t ces .
docker run -it ces bash
```

## Reproduce Results
### Extract Program Properties
To extract the program properties required by CES, please run the following command:
```
bash scripts/extract_properties.sh
```
### RQ1. Performance in CES
To reprodeuce LLMs' performance on CES, please run the folliwing command:
```
bash scripts/run_ces.sh $MODEL_ID $DATASET $CACHE_DIR
```

`MODEL_ID`: Currently CES supports following models:  ```codellama/CodeLlama-13b-Instruct-hf```, ```codellama/CodeLlama-13b-hf```,  ```codellama/CodeLlama-13b-Instruct-hf```,```codellama/CodeLlama-7b-hf```,  
```codellama/CodeLlama-7b-Instruct-hf```, ```codellama/CodeLlama-34b-Instruct-hf``` ```codellama/CodeLlama-13b-hf```,```deepseek-ai/deepseek-coder-6.7b-instruct```, ```deepseek-ai/deepseek-coder-33b-instruct```,```deepseek-ai/deepseek-coder-6.7b-base```, ```bigcode/starcoder2-15b```, ```gpt-4-turbo```,
```gemini/gemini-1.5-pro```, ```semcoder/semcoder_s, deepseek-r1, gemini/gemini-2.5-pro-preview-05-06, o4-mini-2025-04-16```

```CACHE_DIR```: the directory to save huggingface model checkpoints.

If you want to evaluate new LLMs with CES, please 
(1) Add the configuration of the model in `model_config.json`
(2) Add your prompt into `src/ces/create_prompts.py` if needed

### RQ2. Reasoning Consistency Across Tests
To reproduce the results in RQ2, please run the following command:
```
bash scripts/run_consistency.sh $MODEL_ID$ $DATASET$
```

### RQ3. Diagnostic Analysis
After prompting LLMs on CES, run the follwoing command to locate the simulation divergence:
```
bash scripts/run_divergence_localization.sh $MODEL_ID$ $DATASET$
```
Annlysis results will be written into `Experiment_Results/summary/incorrect_output/{model_id}_{dataset}.json`
And we will also print results, for example
```
V_l, I_l, P_c, B_c
======LO======
0_1_X_X: 1
1_0_X_X: 1
======CO======
X_X_0_0: 3
======LC======
0_1_X_X: 12
X_X_0_0: 11
0_0_X_X: 5
1_0_X_X: 7
```
Definations of symbols can be found in the RQ3 in the paper.

### RQ4. CES and Bug-Related Tasks
To compare an LLM’s performance on bug repair, bug prediction, bug localization, and CES, run:
```
bash scripts/run_bug_tasks.sh $MODEL_ID HumanEvalFix $CACHE_DIR
```
Then use the CES framework to perform a reliable analysis of the model’s performance on bug-related tasks:
```
bash scripts/analyze_bug_tasks.sh $MODEL_ID HumanEvalFix
```
This command generate JSON reports under `./Experiment_Results/summary/bug_task_analysis`, and  print key statistics in the console, for example:
```
======Bug Repair gpt-4-turbo  HumanEvalFix ======
confident success: 44
suspicious success: 13
likely success: 57
incoherent: 32
======Bug Localization gpt-4-turbo  HumanEvalFix ======
confident success: 32
suspicious success: 9
likely success: 48
incoherent: 23
======Bug Prediction gpt-4-turbo  HumanEvalFix ======
confident success: 43
suspicious success: 13
likely success: 52
incoherent: 31
```


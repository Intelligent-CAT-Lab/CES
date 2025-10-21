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
```codellama/CodeLlama-7b-Instruct-hf```, ```codellama/CodeLlama-34b-Instruct-hf``` ```codellama/CodeLlama-13b-hf```,```deepseek-ai/deepseek-coder-6.7b-instruct```, ```deepseek-ai/deepseek-coder-33b-instruct```,```deepseek-ai/deepseek-coder-6.7b-base```, ```ise-uiuc/Magicoder-S-DS-6.7B```, ```bigcode/starcoder```, ```bigcode/starcoder2-15b```, ```gpt-4-turbo```,
```gemini/gemini-1.5-pro```, ```semcoder/semcoder_s, deepseek-r1, gemini/gemini-2.5-pro-preview-05-06, o4-mini-2025-04-16```

```CACHE_DIR```: the directory to save huggingface model checkpoints.

If you want to evaluate new LLMs with CES, please 
(1) Add the configuration of the model in `model_config.json`
(2) Add your prompt into `src/ces/create_prompts.py` if needed

### RQ2. Reasoning Consistency Across Tests
To reproduce the results in RQ2, please run the following command:
```
bash scripts/run_consistency.sh $MODEL_ID$
```

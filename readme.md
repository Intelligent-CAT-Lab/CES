# CES: Assessing Coherency and Consistency of Code Execution Reasoning by Large Language Models
Artifact for the paper Assessing Coherency and Consistency of Code Execution Reasoning by Large Language Models, accepted by XXXX.
Authors are Changshu Liu, Yang Chen, and Reyhaneh Jabbarvand.

## Getting Started
Run the following commands to install all the dependencies on your local machine:
```
conda create -n ces python=3.8
conda activate ces
pip install -r requirements.txt
```

Then go to `config/model_config.json` and edit the file with your OpenAI/Google AI Studio key.

Alternatively, we provide a Dockerfile to reproduce the results of CES.
Please download [Docker](https://www.docker.com/) and and then execute the following to create a docker image and execute the container in interactive mode:

```
docker build -t ces .
docker run -it ces bash
```

## Reproduce Results
### RQ1. Performance in CES
To reprodeuce LLMs' performance on CES, please run the folliwing command:
```
bash scripts/run_ces.sh $MODEL_ID $DATASET $CACHE_DIR
```

`MODEL_ID`: Currently CES supports following models:  ```codellama/CodeLlama-13b-Instruct-hf```, ```codellama/CodeLlama-13b-hf```,  ```codellama/CodeLlama-13b-Instruct-hf```,```codellama/CodeLlama-7b-hf```,  
```codellama/CodeLlama-7b-Instruct-hf```, ```codellama/CodeLlama-34b-Instruct-hf``` ```codellama/CodeLlama-13b-hf```,```deepseek-ai/deepseek-coder-6.7b-instruct```, ```deepseek-ai/deepseek-coder-33b-instruct```,```deepseek-ai/deepseek-coder-6.7b-base```, ```ise-uiuc/Magicoder-S-DS-6.7B```, ```bigcode/starcoder```, ```bigcode/starcoder2-15b```, ```gpt-4-turbo```,
```gemini/gemini-1.5-pro```, ```semcoder/semcoder_s, deepseek-r1, gemini/gemini-2.5-pro-preview-05-06, o4-mini-2025-04-16```

```CACHE_DIR```: the directory to save huggingface model checkpoints.

### RQ2. Reasoning Consistency Across Tests

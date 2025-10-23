import json
import sys
def copy_files(dataset):
    path = f"./src/prime_path_extraction/{dataset}_prime_path_coverage.jsonl"
    dest_folder = f"./dataset/{dataset}"
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():                 # skip blank lines
                obj = json.loads(line)
                problem_id = obj['id']
                json_path = f"{dest_folder}/{problem_id}/prime_path.json"
                with open(json_path, 'w') as wr:
                    json.dump(obj, wr, indent=4)
if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        copy_files(args[0])
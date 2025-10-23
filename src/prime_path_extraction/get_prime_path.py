import ast
import coverage
import subprocess
import os
import sys
import json
import pygraphviz as pgv
import networkx as nx
from py2cfgPlus.builder import CFGBuilder
# please do include folder py2cfgPlus in the project path as it's built with local modifications based on original py2cfg

def initialize_jsonl(filename):
    with open(filename, 'w') as file:
        file.write('\n')

def write_jsonl(filename, data):
    with open(filename, 'a') as file:
        file.write(json.dumps(data) + '\n')

def extract_all_simple_paths(graph):
    nodes = list(graph.nodes)
    all_paths = []
    for start_node in nodes:
        for end_node in nodes:
            if start_node != end_node:
                paths = list(nx.all_simple_paths(graph, start_node, end_node))
                all_paths.extend(paths)
    return all_paths

def is_prime_path(path, all_paths):
    # longest simple path that is not sub of others
    for other_path in all_paths:
        if path != other_path and len(path) <= len(other_path):
            if any(path == other_path[i:i+len(path)] for i in range(len(other_path) - len(path) + 1)):
                return False
    return True

def generate_prime_paths(cfg):
    all_paths = extract_all_simple_paths(cfg)
    prime_paths = [path for path in all_paths if is_prime_path(path, all_paths)]
    return prime_paths

def get_prime_paths(python_file, logsdir, cfg_id):
    cfg_builder = CFGBuilder()
    cfg = cfg_builder.build_from_file('CFG', python_file)
    cfg.build_visual(f'{cfg_id}_CFG', 'dot')
    cfg.build_visual(f'{cfg_id}_CFG', 'png')
    G = pgv.AGraph(f"{cfg_id}_CFG.dot")
    nx_graph = nx.nx_agraph.from_agraph(G)
    # for node in nx_graph.nodes:
    #     print(nx_graph.nodes[node]['label'])
    #     print(nx_graph.nodes[node]['linenum'])
    
    prime_paths = generate_prime_paths(nx_graph)
    prime_paths_stats = []
    prime_paths_linenums = []
    for path in prime_paths:
        stats = [nx_graph.nodes[node].get('label') for node in path]
        linenums = []
        for node in path:
            linenums.extend([ast.literal_eval(nx_graph.nodes[node].get('linenum'))])
        prime_paths_stats.append(stats)
        # print("Prime Path:", linenums) # stats
        prime_paths_linenums.append(linenums)
    os.makedirs(os.path.dirname(logsdir), exist_ok=True)
    cfg_png = f'{logsdir}/{cfg_id}_CFG.png'
    cfg_dot = f'{logsdir}/{cfg_id}_CFG.dot'
    os.rename(f'{cfg_id}_CFG.png', cfg_png)
    os.rename(f'{cfg_id}_CFG.dot', cfg_dot)
    return prime_paths, prime_paths_stats, prime_paths_linenums, nx_graph, cfg_png, cfg_dot


def run_coverage(script):
    try:
        subprocess.run(['coverage', 'run', script], check=True)
        result = subprocess.run(['coverage', 'report', '-m'], check=True, capture_output=True, text=True)
        write_file(script + "_cov.txt", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error while running coverage: {e.stderr}")
    
    cov = coverage.Coverage()
    cov.load()
    covered_statements_linenos = []
    missing_statements_linenos = []
    for filename in cov.get_data().measured_files():
        executed_lines = cov.get_data().lines(filename)
        for line in executed_lines:
            # print(line)
            covered_statements_linenos.append(line)
        missing_statements_linenos = cov.analysis(filename)[2]
        # print(f"Covered statements in {filename}: {sorted(executed_lines)} Missing statements: {sorted(missing_statements_linenos)}")
    
    subprocess.run(['coverage', 'erase'], check=True)

    return covered_statements_linenos, missing_statements_linenos


def run_coverage_Avatar(script, input_str):
    try:
        # subprocess.run(['printf', f'"{input_str}\n"', '|', 'coverage', 'run', script], check=True)
        # result = subprocess.run(['coverage', 'report', '-m'], check=True, capture_output=True, text=True)
        cmd = [sys.executable, "-m", "coverage", "run", script]
        subprocess.run(
            cmd,
            input=f"{input_str}\n",
            text=True,
            capture_output=True,
            timeout=60
        )
        result = subprocess.run(['coverage', 'report', '-m'], check=True, capture_output=True, text=True)
        write_file(script + "_cov.txt", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error while running coverage: {e.stderr}")
    
    cov = coverage.Coverage()
    cov.load()
    covered_statements_linenos = []
    missing_statements_linenos = []
    for filename in cov.get_data().measured_files():
        executed_lines = cov.get_data().lines(filename)
        for line in executed_lines:
            # print(line)
            covered_statements_linenos.append(line)
        missing_statements_linenos = cov.analysis(filename)[2]
        # print(f"Covered statements in {filename}: {sorted(executed_lines)} Missing statements: {sorted(missing_statements_linenos)}")
    
    subprocess.run(['coverage', 'erase'], check=True)

    return covered_statements_linenos, missing_statements_linenos

def read_file(file_path):
    file = open(file_path, 'r')
    content = file.read()
    return content

def write_file(file_path,content):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    except:
        pass
    f = open(file_path, "w")
    f.write(content)
    f.close()
    
def get_prime_path_coverage(prime_paths, missing_statements_linenos, combination_file, nx_graph):
    missing_statements = [get_statement_from_line(combination_file, lineno) for lineno in missing_statements_linenos]
    covered_paths = []
    missing_paths_linenums = []
    for prime_path in prime_paths:
        prime_path_linenos = []
        for node in prime_path:
            prime_path_linenos.extend([ast.literal_eval(nx_graph.nodes[node]['linenum'])])
        path_missed = bool(set(prime_path_linenos) & set(missing_statements_linenos))
        if not path_missed:
            covered_paths.append(prime_path_linenos)
        else:
            # print("Missing paths (linenums):", prime_path_linenos)
            missing_paths_linenums.append(prime_path_linenos)
            
    # print("#Covered prime paths:", len(covered_paths), "\n#Total prime paths:",len(prime_paths))
    
    return covered_paths, missing_paths_linenums

def get_statement_from_line(file_path, line_number):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        if 1 <= line_number <= len(lines):
            return lines[line_number - 1].strip()
        else:
            return f"Error: Line number {line_number} is out of range. The file has {len(lines)} lines."

    except FileNotFoundError:
        return f"Error: The file {file_path} was not found."
    except Exception as e:
        return f"An error occurred: {e}"
    
def generate_coverage(python_file, input_file, humaneval_id, logsdir):
    print(python_file)
    os.makedirs(os.path.dirname(logsdir), exist_ok=True)
    combination_file = f"{logsdir}/{python_file}"
    if "Avatar" not in python_file:
        write_file(combination_file, f"{read_file(python_file)}\n{read_file(input_file)}")
    else:
        write_file(combination_file, f"{read_file(python_file)}")
    prime_paths, prime_paths_stats, prime_paths_linenums, nx_graph, cfg_png, cfg_dot = get_prime_paths(combination_file, logsdir, humaneval_id)
    if "Avatar" not in python_file:
        covered_statements_linenos, missing_statements_linenos = run_coverage(combination_file)
    else:
        input_str = read_file(input_file).strip()
        covered_statements_linenos, missing_statements_linenos = run_coverage_Avatar(combination_file, input_str)
    covered_paths, missing_paths_linenums = get_prime_path_coverage(prime_paths, missing_statements_linenos, combination_file, nx_graph)
    # print(prime_paths, prime_paths_stats, prime_paths_linenums)
    # print(covered_statements_linenos, missing_statements_linenos)
    # print(covered_paths, missing_paths_linenums)
    results = {
        "id": humaneval_id,
        "python_file": python_file.replace("/home/yang/humaneval_inputs/", ""),
        "input_file": input_file.replace("/home/yang/humaneval_inputs/", ""),
        "prime_paths_nodes": prime_paths,
        "prime_paths_statements": prime_paths_stats,
        "prime_paths_linenumbers": prime_paths_linenums,
        "covered_statements_linenumbers": covered_statements_linenos,
        "missing_statements_linenumbers": missing_statements_linenos,
        "covered_prime_paths_linenumbers": covered_paths,
        "missing_prime_paths_linenumbers": missing_paths_linenums,
        "num_total_prime_paths": len(prime_paths_linenums),
        "num_covered_paths": len(covered_paths),
        "prime_path_coverage": round(len(covered_paths)/len(prime_paths_linenums), 2),
        "cfg_png": cfg_png,
        "cfg_dot": cfg_dot
    }
    return results

def main(humaneval_folder, savetojson, logsdir):
    inputs = {}
    for dirpath, _, files in os.walk(humaneval_folder):
        for file in files:
            humaneval_id = dirpath.split("/")[-1]
            # if "HumanEval_" not in humaneval_id:
            #     continue
            if humaneval_id not in inputs:
                inputs[humaneval_id] = {"main_path": "", "input_path": ""}
            if file == "main.py":
                main_path = os.path.join(dirpath, file)
                inputs[humaneval_id]["main_path"] = main_path
            elif file == "input.txt":
                input_path = os.path.join(dirpath, file)
                inputs[humaneval_id]["input_path"] = input_path
    for humaneval_id in inputs:
        print(humaneval_id, inputs[humaneval_id])
        try:
            results = generate_coverage(inputs[humaneval_id]["main_path"], inputs[humaneval_id]["input_path"], humaneval_id, logsdir)
            write_jsonl(savetojson, results)
        except Exception as e:
            print(humaneval_id, e)
        # results = generate_coverage(inputs[humaneval_id]["main_path"], inputs[humaneval_id]["input_path"], humaneval_id, logsdir)
        # write_jsonl(savetojson, results)

if __name__ == "__main__":
    args = sys.argv[1:]
    datafolder =  f"./dataset/{args[0]}"
    savetojson = f"./src/prime_path_extraction/{args[0]}_prime_path_coverage.jsonl"
    logsdir = f"./src/prime_path_extraction/logs_{args[0]}"
    initialize_jsonl(savetojson)
    main(datafolder, savetojson, logsdir)
    
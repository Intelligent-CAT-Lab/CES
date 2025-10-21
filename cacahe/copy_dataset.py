import os
import shutil

src_folder = "/home/changshu/CODEMIND/dataset/humaneval"
dest_folder = "/home/changshu/Artifacts/CES/dataset/humaneval"

for d in os.listdir(src_folder):
    src_path = os.path.join(src_folder, d)
    dest_path = os.path.join(dest_folder, d)
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    src_file = os.path.join(src_path, "main.py")
    dest_file = os.path.join(dest_path, "main.py")
    if not os.path.exists(dest_file):
        shutil.copy(src_file, dest_file)
    
    src_file_input = os.path.join(src_path, "input.txt")
    dest_file_input = os.path.join(dest_path, "input.txt")
    if not os.path.exists(dest_file_input):
        shutil.copy(src_file_input, dest_file_input)
    
    src_file_output = os.path.join(src_path, "output.txt")
    dest_file_output = os.path.join(dest_path, "output.txt")
    if not os.path.exists(dest_file_output):
        shutil.copy(src_file_output, dest_file_output)   
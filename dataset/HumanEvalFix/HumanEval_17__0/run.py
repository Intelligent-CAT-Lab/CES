from typing import List


def parse_music(music_string: str) -> List[int]:
    note_map = {'o': 3, 'o|': 2, '.|': 1}
    return [note_map[x] for x in music_string.split(' ') if x]

output = parse_music('o| .| o| .| o o| o o|')

file = open("/home/changshu/CODEMIND/dataset/Intermediate/Repair/HumanEvalFix_new/HumanEval_17__0/output.txt", 'w')
file.write(str(output))
file.close()
    
from icecream import ic
import time

test_data = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

with open(r"2023\Day15\input.txt") as f:
    input = f.read()

def parse_input(input_string):
    strings = input_string.strip().split(',')
    return strings

def part_1(input_string):
    data = parse_input(input_string)
    res = 0

    for step in data:
        res += hash_string(step)    
    
    return res

def hash_string(step):
    curr = 0
    for c in step:
        curr = hash_character(c, curr)
    return curr

def hash_character(c, curr):
    curr += ord(c)
    curr = curr * 17
    curr = curr % 256
    return curr

def act(box, step):
    for lens in box:
        if step[0] == lens[0]:
            if step[1] != '':
                lens[1] = step[1]
            else:
                box.remove(lens)
            return None
    if step[1] != '':
        box.append(step)
    return None

def part_2(input_string):
    data = parse_input(input_string)
    boxes = {}

    for step in data:
        step = step.split('=' if step.find("=") >= 0 else '-')
        box_nb = hash_string(step[0])
        boxes.setdefault(box_nb, [])
        act(boxes[box_nb], step)        

    res = 0
    for box_nb, lenses in boxes.items():
        box_power = box_nb + 1
        for i in range(len(lenses)):
            res += box_power * (i + 1) * int(lenses[i][1])

    return res

start_time = time.perf_counter()
result1 = part_1(input)
result2 = part_2(input)
ic(result1, result2)
elapsed_time = time.perf_counter() - start_time

print(f"Time elapsed : {elapsed_time}s")
from icecream import ic
import time
from math import lcm

test_data = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

test_data_2 = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

START_1 = 'AAA'
END_1 = 'ZZZ'

with open(r"2023\Day8\input.txt") as f:
    input = f.read()

def parse_input(input_string):
    res = input_string.strip().split('\n\n')
    instructions = [0 if char == 'L' else 1 for char in res[0]]
    nodes = res[1].strip().split('\n')
    nodes_dict = {}
    for node in nodes:
        directions = node.split('=')[1].strip().split(',')
        left = directions[0].strip().replace('(','')
        right = directions[1].strip().replace(')','')
        nodes_dict[node.split('=')[0].strip()] = (left, right)

    return instructions, nodes_dict

def part_1(input_string):
    instructions, nodes = parse_input(input_string)
    steps = 0
    curr = START_1
    instruction_nb = 0
    while curr != END_1:
        instruction = instructions[instruction_nb]
        curr = get_next_node(instruction, curr, nodes)
        steps += 1
        if instruction_nb < len(instructions) - 1:
            instruction_nb += 1
        else:
            instruction_nb = 0

    return steps

def get_next_node(instruction, current_node, nodes):
    return nodes[current_node][instruction]

def part_2(input_string):
    instructions, nodes = parse_input(input_string)
    starting_nodes = [node for node in nodes if node.endswith('A')]

    res = 1
    for curr in starting_nodes:

        steps = 0
        instruction_nb = 0
        while not curr.endswith('Z'):
            instruction = instructions[instruction_nb]
            curr = get_next_node(instruction, curr, nodes)
            steps += 1
            if instruction_nb < len(instructions) - 1:
                instruction_nb += 1
            else:
                instruction_nb = 0
        res = lcm(res, steps)
    
    return res

start_time = time.perf_counter()
result1 = part_1(input)
result2 = part_2(input)
ic(result1, result2)
elapsed_time = time.perf_counter() - start_time

print(f"Time elapsed : {elapsed_time}s")
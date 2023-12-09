from icecream import ic
import time
from math import lcm

test_data = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
8 10 9 -2 -17 8
0 1 1 0
"""

with open(r"2023\Day9\input.txt") as f:
    input = f.read()

def parse_input(input_string):
    lines = [[int(x) for x in line.split()] for line in input_string.strip().split('\n')]
    return lines

def part_1(input_string):
    data = parse_input(input_string)
    ic(data)
    last_vals = []
    for sequence in data:
        last_vals.append(get_next_val(sequence))
    ic(last_vals)
    return sum(last_vals)

def get_next_val(sequence):
    if not any(sequence):
        return 0
    lower_sequence = []
    for i in range(len(sequence) - 1):
        diff = sequence[i + 1] - sequence[i]
        lower_sequence.append(diff)
    return sequence[-1] + get_next_val(lower_sequence)

def part_2(input_string):
    data = parse_input(input_string)
    last_vals = []
    for sequence in data:
        sequence.reverse()
        last_vals.append(get_next_val(sequence))
    return sum(last_vals)

start_time = time.perf_counter()
result1 = part_1(input)
result2 = part_2(input)
ic(result1, result2)
elapsed_time = time.perf_counter() - start_time

print(f"Time elapsed : {elapsed_time}s")
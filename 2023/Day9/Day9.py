from icecream import ic
import time
from math import lcm

test_data = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

with open(r"2023\Day9\input.txt") as f:
    input = f.read()

def parse_input(input_string):
    return input_string

def part_1(input_string):
    data = parse_input(input_string)
    return data

def part_2(input_string):
    data = parse_input(input_string)
    return data

start_time = time.perf_counter()
result1 = part_1(input)
result2 = part_2(input)
ic(result1, result2)
elapsed_time = time.perf_counter() - start_time

print(f"Time elapsed : {elapsed_time}s")
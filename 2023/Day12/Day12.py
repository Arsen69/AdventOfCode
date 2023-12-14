from icecream import ic
import time
from functools import cache

test_data = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

DP = {}

with open(r"2023\Day12\input.txt") as f:
    input = f.read()

def parse_input(input_string):
    lines = input_string.strip().split('\n')
    data = []
    for line in lines:
        springs, groups = line.split()
        data.append((springs, groups))
    return data

def part_1(input_string):
    data = parse_input(input_string)
    res = 0
    for line in data:
        spring = line[0]
        counts = [int(nb) for nb in line[1].split(',')]
        DP.clear()
        res += compute(spring, counts, 0, 0, 0)
    return res

def compute(spring, counts, i, count_i, current):
    key = (i, count_i, current)
    if key in DP:
        return DP[key]
    if i == len(spring):
        if count_i == len(counts) and current == 0:
            return 1
        if count_i == len(counts) - 1 and counts[count_i] == current:
            return 1
        return 0
    res = 0
    for c in ['.', '#']:
        if spring[i] == c or spring[i] == '?':
            if c == '.' and current == 0:
                res += compute(spring, counts, i+1, count_i, 0)
            if c == '.' and current > 0 and count_i < len(counts) and counts[count_i] == current:
                res += compute(spring, counts, i+1, count_i+1, 0)
            if c == '#':
                res += compute(spring, counts, i+1, count_i, current+1)
    DP[key] = res
    return res
    
def part_2(input_string):
    data = parse_input(input_string)
    res = 0
    for line in data:
        spring = line[0]
        counts = line[1]
        spring = '?'.join([spring, spring, spring, spring, spring])
        counts = ','.join([counts, counts, counts, counts, counts])
        counts = [int(x) for x in counts.split(',')]
        DP.clear()
        res += compute(spring, counts, 0, 0, 0)
    return res


start_time = time.perf_counter()
result1 = part_1(input)
result2 = part_2(input)
ic(result1, result2)
elapsed_time = time.perf_counter() - start_time

print(f"Time elapsed : {elapsed_time}s")
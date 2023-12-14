from icecream import ic
import time
import numpy as np

test_data = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

with open(r"2023\Day13\input.txt") as f:
    input = f.read()

def parse_input(input_string):
    patterns = input_string.strip().split('\n\n')
    patterns = [np.array([[c for c in line] for line in pattern.split('\n')]) for pattern in patterns]

    return patterns

def execute(input_string, part1):
    patterns = parse_input(input_string)
    summarize = 0
    diffs_allowed = 0 if part1 else 1
    for pattern in patterns:
        pattern_transposed = pattern.transpose()
        for i in range(len(pattern) - 1):
            if is_reflection_line(pattern, i, diffs_allowed):
                summarize += 100 * (i + 1)
        for i in range(len(pattern_transposed) - 1):
            if is_reflection_line(pattern_transposed, i, diffs_allowed):
                summarize += i + 1
    return summarize

def is_reflection_line(pattern, index, diffs_allowed):
    n = 0
    diffs = 0
    while 0 <= index - n < index + n + 1 < len(pattern):
        for j in range(len(pattern[0])):
            if pattern[index - n][j] != pattern[index + n + 1][j]:
                diffs += 1
        n += 1
    if diffs == diffs_allowed:
        return True
    return False

start_time = time.perf_counter()
result1 = execute(input, True)
result2 = execute(input, False)
ic(result1, result2)
elapsed_time = time.perf_counter() - start_time

print(f"Time elapsed : {elapsed_time}s")
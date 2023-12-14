from icecream import ic
import time
import numpy as np

test_data_tilt = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

test_data_count = """
OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
"""

with open(r"2023\Day14\input.txt") as f:
    input = f.read()

def parse_input(input_string):
    lines = input_string.strip().split('\n')
    tab = np.array([[c for c in line] for line in lines])
    return lines, tab

def part_1(input_string):
    lines, tab = parse_input(input_string)
    
    return get_load(tilt_north_part_1(tab))

def tilt_north_part_1(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == 'O':
                new_i = i
                while new_i > 0 and tab[new_i - 1][j] == '.':
                    new_i -= 1
                tab[i][j] = '.'
                tab[new_i][j] = 'O'
    return tab

def tilt_west_part_2(tab):
    for i in range(len(tab)):
        line = ''.join(tab[i])
        while line.find('O.') >= 0:
            line = line.replace('O.', '.O')
        tab[i] = [c for c in line]
    return tab

def get_load(lines):
    res = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if(lines[i][j] == 'O'):
                res += len(lines[i:])
    return res

def apply_n_times(f, x, n):
    """
    Apply `f` to `x` `n` times, returning the result.
    Assumes `f` is deterministic and takes one hashable argument.
    Saves time by finding the first cycle, calculating its length, and using that to skip ahead.
    """
    seen = {}
    for i in range(n):
        if x in seen:
            break
        seen[x] = i
        x = f(x)
    else:
        return x

    cycle_start = seen[x]
    cycle_len = i - cycle_start
    ic(cycle_start, cycle_len)
    remaining = (n - i) % cycle_len
    return apply_n_times(f, x, remaining)

def cycle_once(input_string):
    tab = np.array([[c for c in line] for line in input_string.strip().split('\n')])
    tab = np.rot90(tab, -1)
    for _ in range(4):
        # tilting west gains a few seconds
        tab = tilt_west_part_2(tab)
        tab = np.rot90(tab, -1)
    tab = np.rot90(tab)
    return '\n'.join([''.join(line) for line in tab])

def part_2(input_string, cycles):
    
    final_lines = apply_n_times(cycle_once, input_string, cycles)
    
    return get_load(final_lines.strip().splitlines())


start_time = time.perf_counter()
result1 = part_1(input)
result2 = part_2(input, 1000000000)
ic(result1, result2)
elapsed_time = time.perf_counter() - start_time

print(f"Time elapsed : {elapsed_time}s")
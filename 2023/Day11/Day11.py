from icecream import ic
import time
import numpy as np
from itertools import combinations

test_data = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

with open(r"2023\Day11\input.txt") as f:
    input = f.read()

def parse_input(input_string):
    image = np.array([[c for c in line] for line in input_string.strip().split('\n')])
    return image

def get_sum_lengths(input_string, expansion):
    image = parse_input(input_string)
    empty_rows, empty_columns, galaxies = parse_universe(image)
    combis = set(combinations(galaxies, 2))
    lengths = []
    for comb in combis:
        i, j = comb[0]
        k, l = comb[1]
        x, y = abs(i - k), abs(j - l)
        for row in empty_rows:
            if row in range(*sorted((i, k))):
                x += expansion - 1
            
        for column in empty_columns:
            if column in range(*sorted((j, l))):
                y += expansion - 1
        lengths.append(x + y)

    return sum(lengths)

def parse_universe(image):
    empty_rows = set(range(0, len(image[0])))
    empty_columns = set(range(0,len(image[0])))
    galaxies = set()
    nb_galaxies = 0
    for i in range(0, len(image)):
        for j in range(0, len(image[0])):
            if image[i][j] == '#':
                nb_galaxies += 1
                image[i][j] = nb_galaxies
                galaxies.add((i,j))
                empty_rows.discard(i)
                empty_columns.discard(j)
    return empty_rows, empty_columns, galaxies

start_time = time.perf_counter()
result1 = get_sum_lengths(input, 2)
result2 = get_sum_lengths(input, 1000000)
ic(result1, result2)
elapsed_time = time.perf_counter() - start_time

print(f"Time elapsed : {elapsed_time}s")
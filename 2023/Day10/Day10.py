from icecream import ic
import time

test_data="""
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""

test_data_2="""
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""

PIPES = {'|' : ['N','S'], '-' : ['E','W'], 'L' : ['N','E'], 'J' : ['N','W'], '7' : ['S','W'], 'F' : ['S','E'], '.' : [], 'S' : ['O', 'O']}


with open(r"2023\Day10\input.txt") as f:
    input = f.read()

def get_next_dirs_from_start(map, start):
    start_row, start_column = start
    west_pipe = map[start_row][start_column - 1]
    east_pipe = map[start_row][start_column + 1]
    north_pipe = map[start_row - 1][start_column]
    south_pipe = map[start_row + 1][start_column]
    next_dirs = []
    if any(dir in 'E' for dir in PIPES[west_pipe]):
        next_dirs.append('W')
        
    if any(dir in 'W' for dir in PIPES[east_pipe]):
        next_dirs.append('E')
        
    if any(dir in 'N' for dir in PIPES[south_pipe]):
        next_dirs.append('S')
    
    if any(dir in 'S' for dir in PIPES[north_pipe]):
        next_dirs.append('S')
    return next_dirs

def get_start_pos(map):
    for i in range(len(map)):
        if any(c in 'S' for c in map[i]):
            j = 0
            carac = map[i][j]
            while carac != 'S':
                j += 1
                carac = map[i][j]
            return (i, j)
    
def go_next(map, pos, dir):
    i, j = pos
    if dir == 'N':
        next_pos = (i - 1, j)
    if dir == 'S':
        next_pos = (i + 1, j)
    if dir == 'W':
        next_pos = (i, j - 1)
    if dir == 'E':
        next_pos = (i, j + 1)

    return next_pos, get_next_dirs(map, dir, (next_pos[0], next_pos[1]))

def get_next_dirs(map, last_dir, pos):
    row, column = pos
    pipe = map[row][column]
    next_possible_dirs = PIPES[pipe]
    if last_dir == 'W':
        from_dir = 'E'
    if last_dir == 'N':
        from_dir = 'S'
    if last_dir == 'S':
        from_dir = 'N'
    if last_dir == 'E':
        from_dir = 'W'
    return [dir for dir in next_possible_dirs if dir != from_dir][0]

def parse_input(input_string):
    map = input_string.strip().split('\n')
    return map

def part_1(input_string):
    map = parse_input(input_string)
    start_pos = get_start_pos(map)

    dirs = get_next_dirs_from_start(map, start_pos)

    next = go_next(map, start_pos, dirs[0]) 
    pos = next[0][0], next[0][1]
    dir = next[1]
    steps = 1
    chemin = set()
    chemin.add(start_pos)
    chemin.add(pos)
    while map[pos[0]][pos[1]] != 'S':
        next = go_next(map, pos, dir)
        pos = next[0][0], next[0][1]
        dir = next[1]
        chemin.add(pos)
        steps += 1
    
    return int(steps/2), chemin, map

def part_2(input_string):
    result_part_1 = part_1(input_string)
    ic(result_part_1[2])
    map = result_part_1[2]
    chemin = result_part_1[1]
    inside = 0

    for i in range(len(map)):
        norths = 0
        for j in range(len(map[i])):
            if (i, j) in chemin:
                pipe_directions = PIPES[map[i][j]]
                if 'N' in pipe_directions:
                    norths += 1
                continue
            if not norths % 2 == 0:
                inside += 1

    return inside

start_time = time.perf_counter()
result1 = part_1(input)[0]
result2 = part_2(input)
ic(result1, result2)
elapsed_time = time.perf_counter() - start_time

print(f"Time elapsed : {elapsed_time}s")
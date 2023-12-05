from icecream import ic
import time

test_data = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

with open(r"C:\Users\aspanier\Documents\Formations\AdventOfCode\2023\Day5\input.txt") as f:
    input = f.read()

def get_seeds(input_string):
    seed_line = input_string.strip().split('\n')[0]
    seeds = seed_line.split(':')[1].split()
    return [int(seed) for seed in seeds]

def get_maps(input_string):
    lines = input_string.strip().split('\n')[2:]
    line_index = 0
    maps = {}
    for i in range(7):
        maps['map_' + str(i + 1)] = []
        while 'map' not in lines[line_index]:
            line_index +=1
        line_index += 1
        while line_index < len(lines) and lines[line_index] != '':
            line = lines[line_index].split()
            destination_range = int(line[0])
            source_range = int(line[1])
            length = int(line[2])
            maps['map_' + str(i + 1)].append([destination_range,source_range,length])
            line_index += 1
    return maps

def part_1(input_string):
    seeds = get_seeds(input_string)
    maps = get_maps(input_string)
    ic(maps)
    for map, lines in maps.items():
        ic(map, lines)
        seeds = [get_new_seed(seed,lines) for seed in seeds]
    return seeds

def get_new_seed(seed, lines):
    for line in lines:
        destination_range = line[0]
        source_range = line[1]
        length = line[2]
        change = source_range <= seed and seed < source_range + length
        if not change:
            continue
        sens = -1 if source_range > destination_range else 1
        incr = abs(source_range-destination_range)
        seed = seed + (sens * incr)
        break
    return seed

def get_seeds_part_2(input_string):
    seed_line = input_string.strip().split('\n')[0]
    seeds = [int(seed) for seed in seed_line.split(':')[1].split()]
    ranges = []
    for i in range(0, len(seeds), 2):
        if i >= len(seeds):
            break
        start = seeds[i]
        end = seeds[i] + seeds[i + 1] - 1
        ranges.append([start, end])
    return ranges
    

def get_new_ranges(range, lines):
    all_treated = []
    working_set = [range]
    
    while working_set != []:
        new_ranges_to_treat = []
        for range_to_treat in working_set:
            for line in lines:
                treated, remainder = treat_line(line, range_to_treat[0], range_to_treat[1])
                if treated:
                    all_treated.append(treated)
                    if remainder:
                        for rest in remainder:
                            new_ranges_to_treat.append(rest)
                    break
        working_set = [new_range for new_range in new_ranges_to_treat]
    return all_treated

def treat_line(line, seed_start, seed_end):
    destination_range_start = line[0]
    source_range_start = line[1]
    length = line[2]
    source_range_end = source_range_start + length - 1

    # seed en dehors de source_range
    if source_range_start > seed_end or seed_start > source_range_end:
        return None, [[seed_start, seed_end]]
    
    sens = -1 if source_range_start > destination_range_start else 1
    incr = abs(destination_range_start - source_range_start)

    # seed in source_range
    if seed_start >= source_range_start and seed_end <= source_range_end:
        new_start = seed_start + (sens * incr)
        new_end = seed_end + (sens * incr)
        return [new_start, new_end], None
    
    # seed strictly larger than source_range
    if seed_start < source_range_start and seed_end > source_range_end:
        new_start = source_range_start + (sens * incr)
        new_end = source_range_end + (sens * incr)
        
        return [new_start, new_end], [[seed_start, source_range_start - 1], [source_range_end + 1, seed_end]]
    # seed start strictly in source_range
    if seed_start > source_range_start and seed_start < source_range_end:
        new_start = seed_start + (sens * incr)
        new_end = source_range_end + (sens * incr)
        return [new_start, new_end], [[source_range_end + 1, seed_end]]
    # seed end strictly in source_range
    if seed_end > source_range_start and seed_end < source_range_end:
        new_start = source_range_start + (sens * incr)
        new_end = seed_end + (sens * incr)
        return [new_start, new_end], [[seed_start, source_range_start - 1]]
    
    # seed start == start source_range
    if seed_start == source_range_start:
        new_start = source_range_start + (sens * incr)
        new_end = source_range_end + (sens * incr)
        return [new_start, new_end], [[source_range_end + 1, seed_end]]
    
    # seed end == end source_range
    if seed_end == source_range_end:
        new_start = source_range_start + (sens * incr)
        new_end = seed_end + (sens * incr)
        return [new_start, new_end], [[seed_start, source_range_start - 1]]
    
    # seed start == end source_range
    if seed_start == source_range_end:
        new_start = seed_start + (sens * incr)
        new_end = source_range_end + (sens * incr)
        return [new_start, new_end], [[seed_start + 1, seed_end]]
    
    # seed end == start source_range
    if seed_end == source_range_start:
        new_start = source_range_end + (sens * incr)
        new_end = seed_end + (sens * incr)
        return [new_start, new_end], [[seed_start, source_range_start - 1]]


def part_2(input_string):
    ranges = get_seeds_part_2(input_string)
    maps = get_maps(input_string)

    for map, translations in maps.items():
        # ic(map, translations)
        new_ranges = []
        for interval in ranges:
            intervals_to_add = get_new_ranges(interval, translations)
            for interval_to_add in intervals_to_add:
                new_ranges.append(interval_to_add)
        ranges = new_ranges

    # ic(ranges)
    min = ranges[0][0]
    for interval in ranges:
        if interval[0] < min:
            min = interval[0]
    return min

start_time = time.time()
result = part_2(input)
elapsed_time = time.time() - start_time

ic(f"Time elapsed : {elapsed_time}s")
from icecream import ic
import time
import math

test_data = """
Time:      7  15   30
Distance:  9  40  200
"""

with open(r"C:\Users\aspanier\Documents\Formations\AdventOfCode\2023\Day6\input.txt") as f:
    input = f.read()

def parse_input(input_string):
    times = [int(time) for time in input_string.strip().split('\n')[0].split(':')[1].split()]
    distances = [int(distance) for distance in input_string.strip().split('\n')[1].split(':')[1].split()]
    return times, distances

def parse_input_2(input_string):
    time = int(''.join([time for time in input_string.strip().split('\n')[0].split(':')[1] if time.isdigit()]))
    distance = int(''.join([distance for distance in input_string.strip().split('\n')[1].split(':')[1] if distance.isdigit()]))
    ic(time,distance)
    return time, distance

def part_1(input_string):
    times, distances = parse_input(input_string)
    possibilities = []
    for i in range(0,len(times)):
        possibilities.append(get_possibilities(times[i], distances[i]))
    return prod(possibilities)

def get_possibilities(time, distance):
    possibilities = 0
    for vitesse in range(time + 1):
        ic(vitesse, vitesse * (time - vitesse))
        if vitesse * (time - vitesse) > distance:
            possibilities += 1
    ic(possibilities)
    return possibilities

def get_possibilities_2(time,distance):
    delta = (time**2 - 4*distance)
    x1 = math.ceil((time - math.sqrt(delta))/2)
    x2 = math.floor((time + math.sqrt(delta))/2)
    return abs(x2 - x1) + 1

def prod(set):
    prod = 1
    for nb in set:
        prod = prod * nb
    return prod

def part_2(input_string):
    time, distance = parse_input_2(input_string)
    return get_possibilities_2(time, distance)

start_time = time.time()
result = part_2(input)
ic(result)
elapsed_time = time.time() - start_time

ic(f"Time elapsed : {elapsed_time}s")
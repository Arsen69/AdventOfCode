from icecream import ic
from collections import defaultdict

with open(r"C:\Users\aspanier\Documents\Formations\AdventOfCode\2023\Day2\input.txt") as f:
    input = f.read()

test_data = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

def get_lignes(input_string):
    lines = [line for line in input_string.strip().split('\n')]
    games_dict = defaultdict()
    for line in lines:
        game, cubes = line.split(':')
        games_dict[int(''.join([charac for charac in game if charac.isdigit()]))] = get_cubes(cubes)
    ic(games_dict)
    return games_dict

def get_cubes(cubes_string):
    tirages = []
    for cube_set in cubes_string.split(';'):
        colors_dict = defaultdict()
        for cubes_colors in cube_set.split(','):
            colors_dict[''.join([charac for charac in cubes_colors if charac.isalpha()])] = int(''.join([charac for charac in cubes_colors if charac.isdigit()]))
        tirages.append(colors_dict)
    return tirages

def check_possible(game_tirage, possible_values):
    for tirage in game_tirage:
        if tirage.get('blue') != None and tirage.get('blue') > possible_values.get('blue'):
            return False
        elif  tirage.get('red') != None and tirage.get("red") > possible_values.get('red'):
            return False
        elif  tirage.get('green') != None and tirage.get('green') > possible_values.get('green'):
            return False
    return True

def get_possibles_values(blue, red, green):
    cubes_available = defaultdict(int)
    cubes_available['blue'] = blue
    cubes_available['red'] = red
    cubes_available['green'] = green
    return cubes_available

def count_possibles(games_tirages, possible_values):
    sum = 0
    for id_game in games_tirages:
        if check_possible(games_tirages.get(id_game), possible_values):
            sum += id_game
    return sum

ic(count_possibles(get_lignes(test_data), get_possibles_values(14,12,13)))

def sum_powers(games_tirages):
    sum = 0
    for id_game in games_tirages:
        ic(games_tirages.get(id_game))
        red, green, blue = get_minimum_cubes(games_tirages.get(id_game))
        sum += red * green * blue
    return sum

def get_minimum_cubes(tirages):
    max_red = 0
    max_green = 0
    max_blue = 0
    for tirage in tirages:
        red = tirage.get('red')
        green = tirage.get('green')
        blue = tirage.get('blue')
        if red != None and max_red < red:
            max_red = red
        if green != None and max_green < green:
            max_green = green
        if blue != None and max_blue < blue:
            max_blue = blue
    return max_red, max_green, max_blue

ic(sum_powers(get_lignes(input)))


input = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

with open(r"C:\Users\aspanier\Documents\Formations\AdventOfCode\2023\Day1\input.txt") as f:
    data = f.read()

def parse_lines_part_1(input):
    lines = [line for line in input.strip().split('\n')]
    lines_numb = []
    for line in lines:
        digits = ''.join([charac for charac in line if charac.isdigit()])
        lines_numb.append(digits[0] + digits[-1])
    return sum([int(numb) for numb in lines_numb])

print(parse_lines_part_1(data))

def parse_lines_part_2(input):
    lines = [line for line in input.strip().split('\n')]
    lines_numb = []
    for line in lines:
        line = line.replace('fiveight','58').replace('threeight','38').replace('oneight','18').replace('eightwo','82').replace('eighthree','83').replace('twone','21').replace('sevenine','79').replace('nineight','98').replace('two','2').replace('one','1').replace('eight','8').replace('three','3').replace('four','4').replace('five','5').replace('six','6').replace('seven','7').replace('nine','9')
        digits = ''.join([charac for charac in line if charac.isdigit()])
        lines_numb.append(digits[0] + digits[-1])
    return sum([int(numb) for numb in lines_numb])

print(parse_lines_part_2(data))
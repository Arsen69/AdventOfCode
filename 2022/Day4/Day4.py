


def parse_input(input):
    pairs = [pair.split(',') for pair in input_string.strip().split('\n')]
    return [(parse_range(pair[0]), parse_range(pair[1])) for pair in pairs]

def parse_range(range_string):
    # Parse range string and return a tuple of start and end
    start, end = map(int, range_string.split('-'))
    return start, end


input_string = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

assignment_pairs = parse_input(input_string)

print(assignment_pairs)
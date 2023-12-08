from icecream import ic

test_data = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

with open(r"2023\Day4\input.txt") as f:
    input = f.read()

def parse_lines(input):
    cards = {}
    for line in input.strip().split('\n'):
        line = line.split(':')
        card = ''.join([char for char in line[0] if char.isdigit()])
        winning = [int(nb) for nb in line[1].split('|')[0].split()]
        having = [int(nb) for nb in line[1].split('|')[1].split()]
        cards[int(card)] = [winning, having]
    return cards

def part_1(cards):
    all_matchs_scores = {}
    for k, v in cards.items():
        winning = v[0]
        having = v[1]
        winning.sort()
        having.sort()
        match = []
        for winning_nb in winning:
            for having_nb in having:
                if winning_nb == having_nb:
                    match.append(winning)
        all_matchs_scores[k]=calcul_score_carte(match)
    return sum(all_matchs_scores.values())

def calcul_score_carte(matchs):
    if(len(matchs) == 0):
        return 0
    return 2**(len(matchs)-1)

def part_2(cards):
    nb_cards = {num: 1 for num in cards.keys()}
    for k, v in cards.items():
        ic(k,nb_cards[k])
        winning = v[0]
        having = v[1]
        match = set(winning).intersection(set(having))
        for i in range(len(match)):
            if k+i+1 > len(nb_cards):
                continue
            nb_cards[k+i+1] += nb_cards[k]
    return sum(nb_cards.values())

ic(part_2(parse_lines(input)))


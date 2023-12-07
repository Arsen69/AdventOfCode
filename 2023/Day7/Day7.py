from icecream import ic
import time

test_data = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

VALUES_1 = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
VALUES_2 = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}
FIVE = 'Five'
FOUR = 'Four'
FULL = 'Full'
THREE = 'Three'
TWO = '2Pair'
ONE = '1Pair'
HIGH = 'High'

with open(r"C:\Users\aspanier\Documents\Formations\AdventOfCode\2023\Day7\input.txt") as f:
    input = f.read()

def parse_hands(input_string):
    return [line.split() for line in input_string.strip().split('\n')]

def part_1(input_string):
    hands_bids = parse_hands(input_string)
    types = {HIGH : [], ONE : [],TWO : [], THREE : [], FULL : [], FOUR : [], FIVE : []}
    for hand_bid in hands_bids:
        hand_bid[1] = int(hand_bid[1])
        types[get_type_part_1(hand_bid[0])].append(hand_bid)
        hand_bid[0] = to_value(hand_bid[0], VALUES_1)

    rank = 1
    total_winning = 0
    for key in types:
        sorted = quicksort(types[key])
        for hand_bid in sorted:
            winning = rank * hand_bid[1]
            total_winning += winning
            rank += 1

    return total_winning
    
def get_type_part_1(hand):
    set_hand = set(hand)
    if len(set_hand) == 1:
        return FIVE
    
    if len(set_hand) == 4:
        return ONE
    
    if len(set_hand) == 5:
        return HIGH
    
    hand_sorted = [card for card in hand]
    hand_sorted.sort()

    if len(set_hand) == 2:
        first_four = hand_sorted[:-1]
        last_four = hand_sorted[1:]
        if len(set(first_four)) == 1 or len(set(last_four)) == 1:
            return FOUR
        return FULL

    if len(set_hand) == 3:
        first_three = hand_sorted[:-2]
        last_three = hand_sorted[2:]
        middle_three = hand_sorted[1:4]
        if len(set(first_three)) == 1 or len(set(last_three)) == 1 or len(set(middle_three)) == 1:
            return THREE
        return TWO

def to_value(hand, VALUES):
    transformed_hand = []
    for card in hand:
        if card.isdigit():
            transformed_hand.append(int(card))
        else:
            transformed_hand.append(VALUES[card])
    return transformed_hand

def is_same_type_stronger(hand1, hand2):
    for i in range(5):
        if hand1[i] != hand2[i]:
            return hand1[i] > hand2[i]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if is_same_type_stronger(pivot[0], x[0])]
        right = [x for x in arr[1:] if is_same_type_stronger(x[0], pivot[0])]
        return quicksort(left) + [pivot] + quicksort(right)

def get_type_part_2(hand):
    hand_sans_j = [card for card in hand if card != 'J']
    nb_j = 5 - len(hand_sans_j)
    set_hand_sans_j = set(hand_sans_j)

    if nb_j == 0:
        return get_type_part_1(hand)
    
    if nb_j == 5 or nb_j == 4:
        return FIVE    

    if nb_j == 3:
        if len(set_hand_sans_j) == 1:
            return FIVE
        return FOUR
    
    if nb_j == 2:
        if len(set_hand_sans_j) == 1:
            return FIVE
        if len(set_hand_sans_j) == 2:
            return FOUR
        return THREE
    
    if nb_j == 1:
        if len(set_hand_sans_j) == 1:
            return FIVE
        
        hand_sorted = [card for card in hand_sans_j]
        hand_sorted.sort()

        if len(set_hand_sans_j) == 2:
            first_three = hand_sorted[0:3]
            last_three = hand_sorted[1:4]
            if len(set(first_three)) == 1 or len(set(last_three)) == 1:
                return FOUR
            return FULL
        
        if len(set_hand_sans_j) == 3:
            return THREE
        
        if len(set_hand_sans_j) == 4:
            return ONE

def part_2(input_string):
    hands_bids = parse_hands(input_string)
    types = {HIGH : [], ONE : [],TWO : [], THREE : [], FULL : [], FOUR : [], FIVE : []}
    for hand_bid in hands_bids:
        hand_bid[1] = int(hand_bid[1])
        types[get_type_part_2(hand_bid[0])].append(hand_bid)
        hand_bid[0] = to_value(hand_bid[0], VALUES_2)

    rank = 1
    total_winning = 0
    for key in types:
        sorted = quicksort(types[key])
        for hand_bid in sorted:
            winning = rank * hand_bid[1]
            total_winning += winning
            rank += 1

    return total_winning

start_time = time.time()
result1 = part_1(input)
result2 = part_2(input)
ic(result1, result2)
elapsed_time = time.time() - start_time

print(f"Time elapsed : {elapsed_time}s")
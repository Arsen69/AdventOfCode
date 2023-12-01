from collections import defaultdict

def create_start(stack: list[str], n_cols: int) -> dict[list]:
    n_cols = n_cols + 1
    start = defaultdict(list)
    letter_indices = range(1, n_cols*4, 4)
    row_indices = range(1, n_cols)

    stack.reverse()

    for row in stack:
        for letter_index, row_index in zip(letter_indices, row_indices):
            if row[letter_index].isalpha():
                start[row_index].append(row[letter_index])

    return start


with open(r"C:\Users\aspanier\Documents\Formations\AdventOfCode\2022\Day5\input.txt") as f:
    text = f.read()

stack, moves = text.split('\n\n')
stack = stack.split('\n')

start = create_start(stack, 9)

def get_moves(moves_string):
    moves=[]
    for move in moves_string.split('\n'):
        indic=[]
        for word in move.split():
            if word.isnumeric():
                indic.append(int(word))
        moves.append(indic)
    return moves     

def move_crates_part1(stack, moves):
    for move in moves:
        for _ in range(move[0]):
            stack.get(move[2]).append(stack.get(move[1])[-1])
            stack.get(move[1]).pop()
    return stack

def move_crates_part2(stack, moves):
    print(stack)
    print(moves)
    for move in moves:
        nb = move[0]
        crates_to_move = stack.get(move[1])[-nb:]
        print(crates_to_move)
        for crate in crates_to_move:
            stack.get(move[2]).append(crate)
        for _ in range(nb):
            stack.get(move[1]).pop()
    return stack

#final1 = move_crates_part1(start, get_moves(moves))
final2 = move_crates_part2(start, get_moves(moves))

def get_sommet(stack):
    #sommets = [stack.get(pile)[-1] for pile in stack.keys()]
    sommets = []
    for pile in stack.keys():
        sommets.append(stack.get(pile)[-1])
    return sommets

#print(''.join(get_sommet(final1)))
print(''.join(get_sommet(final2)))
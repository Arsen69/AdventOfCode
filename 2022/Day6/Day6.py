
input1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
result1 = 7
input2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
result2 = 5

input3 = "nppdvjthqldpwncqszvftbrmjlhg" 
result3 = 6
input4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
result4 = 10
input5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
result5 = 11

with open(r"C:\Users\aspanier\Documents\Formations\AdventOfCode\2022\Day6\input.txt") as f:
    input = f.read()

def find_first_diff_set(input, nb_distinct):
    quatres_derniers = []
    for index, letter in enumerate(input):
        quatres_derniers.append(letter)
        if len(set(quatres_derniers)) == nb_distinct:
            print(quatres_derniers)
            print(set(quatres_derniers))
            return index + 1
        if index + 1 >= nb_distinct:
            quatres_derniers.remove(quatres_derniers[0])

print(find_first_diff_set(input, 4))
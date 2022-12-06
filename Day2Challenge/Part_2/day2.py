# A = rock, B = Paper, C = scissors
# ----- your input
# X = lose, Y = draw, Z = win

splitLines = []
selectionMapping = {
    **dict.fromkeys(['A Y', 'B X', 'C Z'], 1), # rock
    **dict.fromkeys(['A Z', 'B Y', 'C X'], 2), # paper
    **dict.fromkeys(['A X', 'B Z', 'C Y'], 3), # scissors
}
winningMap = { 'X': 0, 'Y': 3, 'Z': 6}

def challenge(lines):
    totalScore = 0
    for entry in lines:
        totalScore += winningMap[entry[2]] + selectionMapping[entry]
    
    return totalScore

with open('input.txt') as file:
    splitLines = file.readlines()
    splitLines = [line.rstrip('\n') for line in splitLines]
    print(challenge(splitLines))
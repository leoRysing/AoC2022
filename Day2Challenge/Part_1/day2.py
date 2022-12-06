# A = rock, B = Paper, C = scissors
# ----- your input
# X = rock, B = Paper, C = scissors

splitLines = []
winningMapping = {
    **dict.fromkeys(['A Z', 'B X', 'C Y'], 0),
    **dict.fromkeys(['A X', 'B Y', 'C Z'], 3),
    **dict.fromkeys(['A Y', 'B Z', 'C X'], 6),
}
selectionMap = { 'X': 1, 'Y': 2, 'Z': 3}

def challenge(lines):
    totalScore = 0
    for entry in lines:
        totalScore += winningMapping[entry] + selectionMap[entry[2]]
    
    return totalScore

with open('input.txt') as file:
    splitLines = file.readlines()
    splitLines = [line.rstrip('\n') for line in splitLines]
    print(len(splitLines))
    print(challenge(splitLines))
# idea; iterate through lines
# find length
# split in half
# for each char in the first half, check if it is in
# the set of characters in the back half

splitLines = []

def charValue(char):
    if (ord(char)) < 97:
        return ord(char) - 38
    else:
        return ord(char) - 96

def findBadge(lines):
    lineSets = [set(line) for line in lines]
    lengths = [len(set) for set in lineSets]
    minSet = lineSets[0]
    nonMinSets = []
    for i in range(1, 3):
        if lengths[i] < len(minSet):
            minSet = lineSets[i]

    nonMinSets = lineSets.copy()
    nonMinSets.remove(minSet)
    # guarenteed to have only one shared item
    for char in minSet:
        if char in nonMinSets[0] and char in nonMinSets[1]:
            print(char, " in group, of value; ", str(charValue(char)))
            return charValue(char)


def challenge(input):
    total = 0
    groups = 0
    for i in range(0, len(input) - 3 + 1, 3):
        total += findBadge(input[i:i+3])
        groups += 1
    print(groups)
    return total

with open('input.txt') as file:
    splitLines = file.readlines()
    splitLines = [line.rstrip('\n') for line in splitLines]
    print(challenge(splitLines))

    
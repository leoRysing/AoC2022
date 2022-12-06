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

def findComLetterVal(str):
    length = len(str)
    mid = length // 2
    secondSet = set(str[mid:length])
    print(secondSet)
    # garuneteed to have exactly one common item
    for i in range(0, mid):
        if str[i] in secondSet:
            return charValue(str[i])

def challenge(input):
    total = 0
    for line in input:
        total += findComLetterVal(line)
    return total

with open('input.txt') as file:
    splitLines = file.readlines()
    splitLines = [line.rstrip('\n') for line in splitLines]
    print(challenge(splitLines))

    
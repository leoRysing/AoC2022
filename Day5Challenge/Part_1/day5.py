from collections import deque

def completeOneInstruction(stacks, instruct):
    instruct = instruct.replace('move ', '').replace(' from ', ',').replace(' to ', ',')
    numToMove, origCol, destCol = tuple(instruct.split(','))
    for i in range(0, int(numToMove)):
        itemToPop = stacks[int(origCol) - 1].pop()
        stacks[int(destCol) - 1].append(itemToPop)

def challenge(input):
    # crates
    crates_part = input[0]
    crates_part = crates_part.split('\n')
    crates_part.reverse()
    cratesLines = crates_part
    crates_num = len("".join(cratesLines[0].split()))

    stacks = [ deque() for i in range(0, crates_num)]

    for i in range(1, len(cratesLines)):
        line = cratesLines[i]
        for j in range(0, crates_num):
            ind = 1 + j * 4
            if line[ind].isalpha(): 
                stacks[j].append(line[ind])
    # "".join(s.split())

    # instructions
    instruct = input[1]
    instructLines = instruct.split('\n')
    for line in instructLines:
        if line != '':
            completeOneInstruction(stacks, line)

    for i in range(0, crates_num):
        if len(stacks[i]) > 0:
            print(stacks[i][-1])

with open('input.txt') as file:
    splitLines = file.read()
    splitLines = splitLines.split('\n\n')
    print(challenge(splitLines))
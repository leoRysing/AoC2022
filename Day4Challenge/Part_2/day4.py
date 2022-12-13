def splitIntoFour(line):
    lineSplits = []
    for item in line:
        for number in item.split('-'):
            if number != '':
                lineSplits.append(int(number))

    return lineSplits

def challenge(input):
    numSubseq = 0
    for line in input:
        inputLine = line.split(',')
        fstL, scndL, fstR, scndR = splitIntoFour(inputLine)
        if ( (fstL <= fstR <= scndL) or
           (fstR <= fstL <= scndR) ):
           numSubseq += 1
    return numSubseq

with open('input.txt') as file:
    splitLines = file.readlines()
    splitLines = [line.rstrip('\n') for line in splitLines]
    print(challenge(splitLines))
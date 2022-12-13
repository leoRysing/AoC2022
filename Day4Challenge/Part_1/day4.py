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
        if ( (fstL <= fstR and scndL >= scndR) or
           (fstR <= fstL and scndR >= scndL) ):
           numSubseq += 1
           print(splitIntoFour(inputLine))
        # conditions; 
        # firstL - secondL <= 0 && firstR - secondR >= 0
        # firstL - secondL >= 0 && firstR - secondR <= 0
    return numSubseq

with open('input.txt') as file:
    splitLines = file.readlines()
    splitLines = [line.rstrip('\n') for line in splitLines]
    print(challenge(splitLines))
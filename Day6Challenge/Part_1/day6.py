
def challenge(line):
    strt, end = 0, 2
    shortSet = set(line[0:3])
    for i in range(3, len(line)):
        end = i
        if line[i] not in shortSet and len(shortSet) == 3:
            return end + 1
        elif line[i] not in shortSet:
            shortSet.add(line[i])
        strt += 1
        shortSet = set(line[strt:end+1])
    

with open('input.txt') as file:
    lines = file.read()
    lines = lines.split('\n')
    print(challenge(lines[0]))
def challenge(line):
    strt, end = 0, 12
    shortSet = set(line[0:13])
    for i in range(13, len(line)):
        end = i
        
        if line[i] not in shortSet and len(shortSet) == 13:
            return end + 1
        elif line[i] not in shortSet:
            shortSet.add(line[i])
        strt += 1
        shortSet = set(line[strt:end+1])

    

with open('input.txt') as file:
    lines = file.read()
    lines = lines.split('\n')
    print(challenge(lines[0]))
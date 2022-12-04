textInput = ""
split = []
# Code to complete the first challenge
# Input split is a list
def challenge(inputSplit):
    # something
    maxCals = -1000
    for elf in inputSplit:
        items = elf.split("\n")
        calTotal = 0
        for item in items:
            if item != '':
                calTotal += int(item)
        maxCals = max(maxCals, calTotal)
    return maxCals

# Driver code to complete the challenge
with open('input.txt') as file:
    textInput = file.read()
    split = textInput.split("\n\n")

print(challenge(split))


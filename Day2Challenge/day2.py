from heapq import heappop, heappush


textInput = ""
split = []
# Code to complete the first challenge
# Input split is a list
def heapAdd(minHeap, nextElf, iteration):
    items = nextElf.split("\n")
    calTotal = 0
    for item in items:
        if item != '':
            calTotal += int(item)
    if iteration < 3:
        heappush(minHeap, calTotal)
    else:
        if calTotal > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, calTotal)
        
def challenge(inputSplit):
    # something
    maxCals = -1000
    # min heap, of size 3
    minHeap = [] # heap of size 3

    i = 0
    for elf in inputSplit:
        heapAdd(minHeap, elf, i)
        i += 1
    return sum(minHeap)

# Driver code to complete the challenge
with open('input.txt') as file:
    textInput = file.read()
    split = textInput.split("\n\n")

print(challenge(split))
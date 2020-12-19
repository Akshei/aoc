import copy, math
def loadFile(isInt = False):
    file = open('abc', 'r')
    passList = [x for x in file]
    for i in range(len(passList)):
        if passList[i][-1] == "\n":
            passList[i] = passList[i][:-1]
    if isInt:
        passList = [int(x) for x in passList]
    return passList

def printAll(listOfStrings):
    for i in listOfStrings:
        print([i])

def LastIndexOf(number, numbersList):
    numbersList= numbersList[::-1]
    index = numbersList.index(number)
    return len(numbersList) -1 - index

numbers = loadFile()
numbers=[int(x) for x in numbers[0].split(',')]
numbersAppeared = dict()
for i in range(len(numbers)):
    numbersAppeared[numbers[i]] = [i]
i = len(numbers) -1
currentNumber = numbers[-1]
everything = list(numbers)
while i < 30000000 + 2:
    lastTurnsOfCurrentNumber = numbersAppeared[currentNumber]
    if len(lastTurnsOfCurrentNumber) == 1:
        currentNumber = 0
    else:
        lastnumber= currentNumber
        currentNumber = lastTurnsOfCurrentNumber[-1] - lastTurnsOfCurrentNumber[-2]
        numbersAppeared[lastnumber].pop(0)
    i += 1
    if currentNumber not in numbersAppeared:
        numbersAppeared[currentNumber] = list()
    numbersAppeared[currentNumber].append(i)
    everything.append(currentNumber)

print(everything[30000000-1])
a = 123
import copy
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

def NeighboursCount(rowNo,colNo,seats):
    amount = 0
    for i in range (-1,2):
        for j in range(-1,2):
            if (i == 0 and j == 0) or (i + rowNo < 0 or j + colNo < 0) or (i + rowNo >= len(seats) or j + colNo >= len(seats[rowNo])):
                continue
            m = 1
            break1 = False
            while break1 is False and seats[rowNo+(i*m)][colNo+(j*m)] == ".":
                m += 1
                if (i == 0 and j == 0) or (rowNo+(i*m) < 0 or colNo+(j*m) < 0) or (rowNo+(i*m) >= len(seats) or colNo+(j*m) >= len(seats[rowNo])):
                    break1 = True
            if break1 is False and seats[rowNo+(i*m)][colNo+(j*m)] == '#':
                amount += 1
    return amount


seats = loadFile()
seatsTemp = loadFile()
similar = False
amount = 0
while similar is False:
    similar = True
    amount = 0
    for rowNo in range(len(seats)):
        for colNo in range(len(seats[rowNo])):
            amountOfNeighbours = NeighboursCount(rowNo,colNo,seats)
            if seats[rowNo][colNo] == 'L' and amountOfNeighbours == 0:
                seatsTemp[rowNo] = seatsTemp[rowNo][:colNo] + '#' + seatsTemp[rowNo][colNo + 1:]
            elif seats[rowNo][colNo] == "#" and amountOfNeighbours >= 5:
                seatsTemp[rowNo] = seatsTemp[rowNo][:colNo] + 'L' + seatsTemp[rowNo][colNo + 1:]
            if seatsTemp[rowNo][colNo] == "#":
                amount += 1
            if seatsTemp[rowNo][colNo] != seats[rowNo][colNo]:
                similar = False
    printAll(seats)
    print()
    seats = copy.deepcopy(seatsTemp)

printAll(seats)
print(amount)
